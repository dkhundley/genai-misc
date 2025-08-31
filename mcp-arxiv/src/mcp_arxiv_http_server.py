#!/usr/bin/env python3

import os
import json
from typing import List

import arxiv
from mcp.server.fastmcp import FastMCP

PAPER_DIR = "papers"

# Initialize the FastMCP server for HTTP transport
mcp = FastMCP("arxiv-research-http")

# Configure host and port for Docker
mcp.settings.host = "0.0.0.0"
mcp.settings.port = 8000

@mcp.tool()
def search_papers(topic: str, max_results: int = 5) -> List[str]:
    '''
    Search for papers on arXiv based on a topic and store their information

    Inputs:
        - topic (str): The topic to search for
        - max_results (int): The maximum number of results to return

    Returns:
        - List[str]: A list of paper titles
    '''

    # Setting the arXiv client
    arxiv_client = arxiv.Client()

    # Searching for the most relevant articles matching the queried topic
    search = arxiv.Search(
        query=topic,
        max_results = max_results,
        sort_by = arxiv.SortCriterion.Relevance
    )

    papers = arxiv_client.results(search)

    path = os.path.join(PAPER_DIR, topic.lower().replace(" ", "_"))
    os.makedirs(path, exist_ok=True)
    file_path = os.path.join(path, "papers_info.json")

    try:
        with open(file_path, "r") as json_file:
            papers_info = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        papers_info = {}

    paper_ids = []
    for paper in papers:
        paper_ids.append(paper.get_short_id())
        paper_info = {
            'title': paper.title,
            'authors': [author.name for author in paper.authors],
            'summary': paper.summary,
            'pdf_url': paper.pdf_url,
            'published': str(paper.published.date())
        }
        papers_info[paper.get_short_id()] = paper_info

    with open(file_path, "w") as json_file:
        json.dump(papers_info, json_file, indent=2)

    print(f'Results are saved in: {file_path}')

    return paper_ids


@mcp.tool()
def extract_info(paper_id: str) -> str:
    '''
    Search for information about a specific paper across all topic directories

    Inputs:
        - paper_id (str): The ID of the paper to extract information from

    Returns:
        - str: A summary of the paper's information
    '''

    for item in os.listdir(PAPER_DIR):
        item_path = os.path.join(PAPER_DIR, item)
        if os.path.isdir(item_path):
            json_file_path = os.path.join(item_path, "papers_info.json")
            try:
                with open(json_file_path, "r") as json_file:
                    papers_info = json.load(json_file)
                    if paper_id in papers_info:
                        paper = papers_info[paper_id]
                        return f"Title: {paper['title']}\nAuthors: {', '.join(paper['authors'])}\nSummary: {paper['summary']}\nPDF URL: {paper['pdf_url']}\nPublished: {paper['published']}"
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f'Error reading {json_file_path}: {str(e)}')
                continue

    return f"There's no saved information related to paper ID: {paper_id}"


@mcp.resource('papers://folders')
def get_available_folders() -> str:
    '''
    List all available topic folders in the papers directory.
    This resource provides a simple list of all available topic folders.
    '''

    folders = []
    
    # Getting all the topic directories
    if os.path.exists(PAPER_DIR):
        for topic_dir in os.listdir(PAPER_DIR):
            topic_path = os.path.join(PAPER_DIR, topic_dir)
            if os.path.isdir(topic_path):
                papers_file = os.path.join(topic_path, "papers_info.json")
                if os.path.exists(papers_file):
                    folders.append(topic_dir)

    content = "# Available Topics\n\n"
    if folders:
        for folder in folders:
            content += f"- {folder}\n"
    else:
        content += "No topics found.\n"

    return content

@mcp.resource('papers://{topic}')
def get_topic_papers(topic: str) -> str:
    '''
    Gets detailed informaiton about papers on a specific topic

    Inputs:
        - topic (str): The topic to get papers for
    '''

    topic_dir = topic.lower().replace(" ", "_")
    papers_file = os.path.join(PAPER_DIR, topic_dir, "papers_info.json")

    if not os.path.exists(papers_file):
        return f"# No papers found for topic: {topic}"

    try:
        with open(papers_file, 'r') as f:
            papers_data = json.load(f)

        content = f"# Papers on {topic.replace("_", " ").title()}\n\n"
        content += f'Total papers: {len(papers_data)}\n\n'

        for paper_id, paper_info in papers_data.items():
            content += f"## {paper_info['title']}\n"
            content += f"- **Authors**: {', '.join(paper_info['authors'])}\n"
            content += f"- **Summary**: {paper_info['summary']}\n"
            content += f"- **PDF URL**: {paper_info['pdf_url']}\n"
            content += f"- **Published**: {paper_info['published']}\n\n"

        return content
    
    except json.JSONDecodeError:
        return f"# Error reading papers data for {topic}\n\nThe papers data file is corrupted."
    

@mcp.prompt()
def generate_search_prompt(topic: str, num_papers: int = 5) -> str:
    '''
    Generate a prompt for Claude to find and discuss academic papers on a specific topic.
    '''
    return f"""Search for {num_papers} academic papers about '{topic}' using the search_papers tool. Follow these instructions:
    1. First, search for papers using search_papers(topic='{topic}', max_results={num_papers})
    2. For each paper found, extract and organize the following information:
       - Paper title
       - Authors
       - Publication date
       - Brief summary of the key findings
       - Main contributions or innovations
       - Methodologies used
       - Relevance to the topic '{topic}'
    
    3. Provide a comprehensive summary that includes:
       - Overview of the current state of research in '{topic}'
       - Common themes and trends across the papers
       - Key research gaps or areas for future investigation
       - Most impactful or influential papers in this area
    
    4. Organize your findings in a clear, structured format with headings and bullet points for easy readability.
    
    Please present both detailed information about each paper and a high-level synthesis of the research landscape in {topic}."""

if __name__ == "__main__":
    # Run the server with streamable HTTP transport
    mcp.run(transport="streamable-http")

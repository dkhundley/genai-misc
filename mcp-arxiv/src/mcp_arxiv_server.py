import json
from typing import List, Dict, Any

import arxiv
from mcp.server.fastmcp import FastMCP

# In-memory storage for papers data
papers_storage: Dict[str, Dict[str, Any]] = {}

def get_all_paper_ids() -> List[str]:
    """Helper function to get all paper IDs across all topics"""
    all_ids = []
    for topic_papers in papers_storage.values():
        all_ids.extend(topic_papers.keys())
    return list(set(all_ids))  # Remove duplicates

def get_topics_list() -> List[str]:
    """Helper function to get all stored topics"""
    return list(papers_storage.keys())

mcp = FastMCP("research")

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

    # Create a topic key for in-memory storage
    topic_key = topic.lower().replace(" ", "_")
    
    # Initialize topic storage if it doesn't exist
    if topic_key not in papers_storage:
        papers_storage[topic_key] = {}

    paper_ids = []
    for paper in papers:
        paper_id = paper.get_short_id()
        paper_ids.append(paper_id)
        paper_info = {
            'title': paper.title,
            'authors': [author.name for author in paper.authors],
            'summary': paper.summary,
            'pdf_url': paper.pdf_url,
            'published': str(paper.published.date())
        }
        papers_storage[topic_key][paper_id] = paper_info

    print(f'Stored {len(paper_ids)} papers for topic "{topic}" in memory')

    return paper_ids


@mcp.tool()
def extract_info(paper_id: str) -> str:
    '''
    Search for information about a specific paper across all stored topics

    Inputs:
        - paper_id (str): The ID of the paper to extract information from

    Returns:
        - str: A summary of the paper's information
    '''

    # Search through all topics in memory
    for topic_key, papers_info in papers_storage.items():
        if paper_id in papers_info:
            paper = papers_info[paper_id]
            return f"Title: {paper['title']}\nAuthors: {', '.join(paper['authors'])}\nSummary: {paper['summary']}\nPDF URL: {paper['pdf_url']}\nPublished: {paper['published']}"

    return f"There's no saved information related to paper ID: {paper_id}"


@mcp.tool()
def get_papers_stats() -> str:
    '''
    Get statistics about papers stored in memory

    Returns:
        - str: Statistics about stored papers
    '''
    
    if not papers_storage:
        return "No papers are currently stored in memory. Use search_papers() to add some papers."
    
    total_topics = len(papers_storage)
    total_papers = sum(len(papers) for papers in papers_storage.values())
    unique_papers = len(get_all_paper_ids())
    
    stats = f"Paper Storage Statistics:\n"
    stats += f"- Total topics: {total_topics}\n"
    stats += f"- Total paper entries: {total_papers}\n"
    stats += f"- Unique papers: {unique_papers}\n\n"
    
    stats += "Topics and paper counts:\n"
    for topic, papers in papers_storage.items():
        readable_topic = topic.replace("_", " ").title()
        stats += f"- {readable_topic}: {len(papers)} papers\n"
    
    return stats


@mcp.tool()
def clear_papers_storage() -> str:
    '''
    Clear all papers from memory storage

    Returns:
        - str: Confirmation message
    '''
    
    if not papers_storage:
        return "Paper storage is already empty."
    
    papers_count = sum(len(papers) for papers in papers_storage.values())
    topics_count = len(papers_storage)
    
    papers_storage.clear()
    
    return f"Cleared {papers_count} papers from {topics_count} topics from memory storage."


@mcp.resource('papers://folders')
def get_available_folders() -> str:
    '''
    List all available topic folders stored in memory.
    This resource provides a simple list of all available topic folders.
    '''

    # Get all topics from memory
    folders = list(papers_storage.keys())

    content = "# Available Topics\n\n"
    if folders:
        for folder in folders:
            # Convert topic key back to readable format
            readable_topic = folder.replace("_", " ").title()
            content += f"- {readable_topic} (key: {folder})\n"
    else:
        content += "No topics found. Use search_papers() to add some topics.\n"

    return content

@mcp.resource('papers://{topic}')
def get_topic_papers(topic: str) -> str:
    '''
    Gets detailed information about papers on a specific topic

    Inputs:
        - topic (str): The topic to get papers for
    '''

    # Convert topic to the same format used for storage keys
    topic_key = topic.lower().replace(" ", "_")
    
    if topic_key not in papers_storage:
        return f"# No papers found for topic: {topic}\n\nUse search_papers('{topic}') to search for papers on this topic."

    papers_data = papers_storage[topic_key]

    if not papers_data:
        return f"# No papers stored for topic: {topic}"

    content = f"# Papers on {topic.replace('_', ' ').title()}\n\n"
    content += f'Total papers: {len(papers_data)}\n\n'

    for paper_id, paper_info in papers_data.items():
        content += f"## {paper_info['title']}\n"
        content += f"- **Paper ID**: {paper_id}\n"
        content += f"- **Authors**: {', '.join(paper_info['authors'])}\n"
        content += f"- **Summary**: {paper_info['summary']}\n"
        content += f"- **PDF URL**: {paper_info['pdf_url']}\n"
        content += f"- **Published**: {paper_info['published']}\n\n"

    return content
    

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
    import sys
    
    # Check command line arguments for transport type
    if len(sys.argv) > 1 and sys.argv[1] == "--http":
        # Run with streamable HTTP transport for curl/REST API access
        print("Starting MCP server with streamable HTTP transport on port 8000...")
        mcp.run(transport="streamable-http", mount_path="/mcp")
    else:
        # Default stdio transport for MCP clients
        mcp.run(transport="stdio")
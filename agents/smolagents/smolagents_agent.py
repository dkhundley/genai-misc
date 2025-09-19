# Importing the necessary Python libraries
import os
import yaml
import logging
import warnings
from datetime import datetime
from typing import Union
from smolagents import CodeAgent, LiteLLMModel, tool

# Suppress all warnings and LiteLLM logging
warnings.filterwarnings("ignore")
os.environ["LITELLM_LOG"] = "ERROR"
logging.getLogger("litellm").setLevel(logging.CRITICAL)
logging.getLogger("litellm.litellm_core_utils.litellm_logging").setLevel(logging.CRITICAL)
logging.getLogger().setLevel(logging.CRITICAL)

# Loading the OpenAI API key from file
with open('../../keys/api_keys.yaml') as f:
    API_KEYS = yaml.safe_load(f)

# Setting the LiteLLM model for OpenAI
model = LiteLLMModel(
    model_id='gpt-4o-mini',
    api_key=API_KEYS['OPENAI_API_KEY']
)

@tool
def perform_calculation(expr: str) -> Union[float, int, str]:
    '''
    Performs a basic mathematical calculation given as a string expression.

    Args:
        expr: A string containing a mathematical expression (e.g., "30 / 5").
    
    Returns:
        The result of the calculation or an error message.
    '''
    try:
        # Setting allowed characters for safety
        allowed_chars = "0123456789+-*/.() "

        # Checking for invalid characters
        if not all(c in allowed_chars for c in expr):
            raise ValueError("Invalid characters in expression.")
        
        # Evaluating the mathematical expression safely
        return eval(expr)
    
    except Exception as e:
        return f"Error: {e}"

@tool
def get_current_datetime() -> str:
    '''
    Returns the current date and time in a human-readable format.

    Returns:
        The current date and time as a string (e.g., "June 9, 2024 at 3:30 PM").
    '''
    return datetime.now().strftime("%B %d, %Y at %I:%M %p")

# Instantiating the agent with only the model (no custom tools)
no_tools_agent = CodeAgent(tools=[], model=model)

# Instantiating the agent with the model and tools
tools_agent = CodeAgent(tools=[perform_calculation, get_current_datetime], model=model)

# Instantiating a "Jar Jar Binks" agent with model, tools, and system message
# Note: smolagents uses different prompt management, so we'll set this via system message in run()
jar_jar_agent = CodeAgent(
    tools=[perform_calculation, get_current_datetime], 
    model=model
)

# Testing the agents with a simple sample prompt
simple_prompt = "What is the capital of Illinois?"

print("No Tools Agent Response:")
response = no_tools_agent.run(simple_prompt)
print(response)
print("\n\nTools Agent Response:")
response = tools_agent.run(simple_prompt)
print(response)
print("\n\nJar Jar Binks Agent Response:")
jar_jar_system_message = "You are Jar Jar Binks from Star Wars. You speak in a distinctive way, often using phrases like 'Meesa' and 'Yousa'. Answer questions and perform tasks in character, adding a touch of humor and clumsiness to your responses."
response = jar_jar_agent.run(f"System: {jar_jar_system_message}\n\nUser: {simple_prompt}")
print(response)

# Testing the agents with a calculation prompt
calc_prompt = "What is 30586450123124918824 * 85748795938829102938?"

print("Actual Calculation:")
print(30586450123124918824 * 85748795938829102938)
print("\n\nNo Tools Agent Response:")
response = no_tools_agent.run(calc_prompt)
print(response)
print("\n\nTools Agent Response:")
response = tools_agent.run(calc_prompt)
print(response)
print("\n\nJar Jar Binks Agent Response:")
response = jar_jar_agent.run(f"System: {jar_jar_system_message}\n\nUser: {calc_prompt}")
print(response)

# Testing the agents with a prompt to get the current date and time
datetime_prompt = "What is the current date and time?"

print("Actual Date and Time:")
print(datetime.now().strftime("%B %d, %Y at %I:%M %p"))
print("\n\nNo Tools Agent Response:")
response = no_tools_agent.run(datetime_prompt)
print(response)
print("\n\nTools Agent Response:")
response = tools_agent.run(datetime_prompt)
print(response)
print("\n\nJar Jar Binks Agent Response:")
response = jar_jar_agent.run(f"System: {jar_jar_system_message}\n\nUser: {datetime_prompt}")
print(response)
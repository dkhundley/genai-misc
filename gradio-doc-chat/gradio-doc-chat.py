# Importing the necessary Python libraries
import os
import json

import pandas as pd

import gradio as gr
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableLambda
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories.in_memory import ChatMessageHistory


## GRADIO UI LAYOUT & FUNCTIONALITY
## ---------------------------------------------------------------------------------------------------------------------
# Defining the building blocks that represent the form and function of the Gradio UI
with gr.Blocks(theme = gr.themes.Base()) as gradio_ui:

    # Display a primary header label
    header_label = gr.Label(value = 'Document Chat', container = False)



## SCRIPT INVOCATION
## ---------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    # Launching the Gradio interface
    gradio_ui.launch()
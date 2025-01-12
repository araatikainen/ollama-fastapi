import os
from langchain_ollama import ChatOllama, OllamaLLM
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from services.system_message import SYSTEM_MESSAGE, SYSTEM_MESSAGE_VISION
from ollama import Client


def format_history(messages: list, vision=False):
    if vision:
        history = [SystemMessage(SYSTEM_MESSAGE_VISION)]
    else:
        history = [SystemMessage(SYSTEM_MESSAGE)]

    for msg in messages:
        if msg["role"] == "user":
            history.append(HumanMessage(msg["content"]))
        if msg["role"] == "assistant":
            history.append(AIMessage(msg["content"]))
    return history


def chat_ollama(data: dict):
    try:
        llm = ChatOllama(
                base_url=os.getenv("OLLAMA_BASE_URL"),
                model=os.getenv("OLLAMA_MODEL"),
                temperature=0.5,
                )
        
        messages = format_history(data["messages"])
        result = llm.invoke(messages)
        print("res", result)
        return result
    except Exception as e:
        raise e
    

def chat_image(data:dict):
    try:
        llm = OllamaLLM(
                base_url=os.getenv("OLLAMA_VISION_BASE_URL"),
                model=os.getenv("OLLAMA_VISION_MODEL"),
                temperature=0.5,
                )
        messages = format_history(data["messages"], vision=True)
        llm = llm.bind(images=[str(data["image"])])
        result = llm.invoke(messages)
        print("res", result)
        return result
    except Exception as e:
        raise e

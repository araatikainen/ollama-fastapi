import os
import requests
from fastapi import APIRouter, HTTPException
from services.langchain import chat_ollama, chat_image
from models.requests import RequestOllama, RequestOllamaVision, ResponseMessage

router = APIRouter()

@router.post("/test")
def generate(data: RequestOllama):
    """Generate a message by sending request to Ollama API endpoint"""
    try:
        print("data:",data)
        res = requests.post(os.getenv("OLLAMA_BASE_URL")+'/api/generate', json={
            "prompt": data["prompt"],
            "stream" : False,
            "model" : "llama3.2"
            })
        return ResponseMessage(status_code=200, content=res.json()["content"])
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
        

@router.post("/generate")
def generate_langchain(request: RequestOllama):
    """Endpoint to generate a message using Ollama model"""
    try:
        result = chat_ollama(request.model_dump())
        return ResponseMessage(status_code=200, content=result.content)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/generate-vision")
def generate_langchain(request: RequestOllamaVision):
    """Endpoint to generate a message using Ollama vision model"""
    try:
        result = chat_image(request.model_dump())
        return ResponseMessage(status_code=200, content=result)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
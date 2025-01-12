from pydantic import BaseModel
from typing import List, Dict, Optional


class RequestOllama(BaseModel):
    messages: List[Dict[str, str]]


class RequestOllamaVision(BaseModel):
    image: Optional[str]
    messages: list


class ResponseMessage(BaseModel):
    status_code: int
    content: str


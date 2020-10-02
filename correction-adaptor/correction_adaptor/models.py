from pydantic import BaseModel
from typing import Optional


Language = str


class BaseMessage(BaseModel):
    text: str


class Message(BaseMessage):
    language: Optional[str]


class CorrectedMessage(BaseMessage):
    text: str
    language: str

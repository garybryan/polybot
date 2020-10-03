# TODO put models in common package that multiple services can use
from pydantic import BaseModel
from typing import Optional


class Message(BaseModel):
    text: str
    language: Optional[str]


class CorrectedMessage(BaseModel):
    language: str
    corrections: list

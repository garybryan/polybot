from pydantic import BaseModel
from typing import List, Optional


class BaseMessage(BaseModel):
    text: str
    language: Optional[str]


class Message(BaseMessage):
    user_language: Optional[str]
    # TODO validate supported language string?


class Suggestion(BaseModel):
    value: str
    short_description: Optional[str]


class Context(BaseModel):
    text: str
    offset: int
    length: int


class Category(BaseModel):
    id: str
    name: str


class Rule(BaseModel):
    id: str
    description: str
    type: str
    urls: Optional[List[str]]
    category: Category


class Correction(BaseModel):
    message: str
    short_message: str
    suggestions: List[Suggestion]
    offset: int
    length: int
    context: Context
    rule: Rule
    sentence: str


class CorrectedMessage(BaseModel):
    language: str
    corrections: List[Correction]

from typing import List, Optional

from pydantic.main import BaseModel

from ...models import (
    BaseMessage,
    Category,
    Context,
)


class LanguageToolMessage(BaseMessage):
    motherTongue: Optional[str]


class LanguageToolRule(BaseModel):
    id: str
    subId: Optional[str]
    description: str
    issueType: str
    urls: Optional[List[str]]
    category: Category


class Replacement(BaseModel):
    value: str
    shortDescription: Optional[str]


class Match(BaseModel):
    message: str
    shortMessage: str
    offset: int
    length: int
    replacements: List[Replacement]
    context: Context
    sentence: str
    rule: LanguageToolRule


class Language(BaseModel):
    code: str


class LanguageToolCorrectedMessage(BaseModel):
    language: Language
    matches: List[Match]

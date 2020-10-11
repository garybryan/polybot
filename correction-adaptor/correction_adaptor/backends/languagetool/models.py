from typing import List, Optional

from pydantic.main import BaseModel

from ...models import (
    BaseMessage,
    Category,
    Context,
)


class LanguageToolMessage(BaseMessage):
    motherTongue: Optional[str]


class URL(BaseModel):
    value: str


class LanguageToolRule(BaseModel):
    id: str
    subId: Optional[str]
    description: str
    issueType: str
    urls: Optional[List[URL]]
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


class LanguageToolLanguage(BaseModel):
    code: str


class LanguageToolCorrectedMessage(BaseModel):
    language: LanguageToolLanguage
    matches: List[Match]

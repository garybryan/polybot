from typing import List, Optional

from pydantic.main import BaseModel

from ...models import (
    BaseMessage,
    CorrectedMessage,
    Message,
    Category,
    Context,
    Suggestion,
)


class LanguageToolMessage(Message):
    motherTongue: Optional[str]


class LanguageToolRule(BaseModel):
    id: str
    subId: Optional[str]
    description: str
    issueType: str
    urls: Optional[List[str]]
    category: Category


class Match(BaseModel):
    message: str
    shortMessage: str
    offset: int
    length: int
    replacements: List[Suggestion]
    context: Context
    sentence: str
    rule: LanguageToolRule


class LanguageToolCorrectedMessage(BaseMessage):
    matches: List[Match]

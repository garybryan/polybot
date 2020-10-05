from typing import List
from fastapi import APIRouter

from ..models import Language

router = APIRouter()


@router.get("/languages", response_model=List[Language])
def get() -> List[Language]:
    return [Language(name="English (British)", code="en-GB")]

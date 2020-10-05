from typing import List
from fastapi import APIRouter

from ..models import Language

# TODO change to backend
from ..backends import get_backend


router = APIRouter()


@router.get("/languages", response_model=List[Language])
def get() -> List[Language]:
    backend = get_backend()
    reply = backend.supported_languages
    return reply

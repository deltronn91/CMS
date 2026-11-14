from pydantic import BaseModel
from typing import Optional


class ConceptCreate(BaseModel):
    title: str
    definition: str
    example: str
    explanation: str
    common_misconception: str
    related_concepts: str | None = None

class UpdateConcept(BaseModel):
    title: Optional[str] = None 
    definition: Optional[str] = None 
    example: Optional[str] = None 
    explanation: Optional[str] = None
    common_misconception: Optional[str] = None 
    related_concepts: Optional[str] = None 



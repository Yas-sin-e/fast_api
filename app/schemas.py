from pydantic import BaseModel, Field
from typing import Annotated
class Prediction(BaseModel):
    label: str
    score: float = Field(ge=0, le=1)
# Un texte individuel doit respecter les mêmes contraintes
# que /detect-language    
TextValue = Annotated[
    str,
    Field(min_length=3, max_length=1000)
]    
class LanguageRequest(BaseModel):
    text: str = Field(min_length=3, max_length=1000)   
    
class LanguageResponse(BaseModel):
    provider: str
    model: str
    latency_ms: float
    language: str
    requires_review: bool
    degraded: bool = False
    predictions: list[Prediction]    
    
# Nouveau schéma pour le batch
class BatchLanguageRequest(BaseModel):
    texts: list[TextValue] = Field(
        min_length=1,
        max_length=10
    )


class BatchLanguageResponse(BaseModel):
    results: list[LanguageResponse]    
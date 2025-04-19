from pydantic import BaseModel, Field
from typing import List, Optional, Annotated

class Book(BaseModel):
    title: str
    author: str
    genre: str
    rating: Optional[float] = Field(None, ge=0, le=5)
    notes: Optional[str] = None

class BookAnalysisRequest(BaseModel):
    book_info: str = Field(..., min_length=1)
    preferences: dict

class BookAnalysisResponse(BaseModel):
    plot_summary: str
    themes: List[str]
    writing_style: str
    reading_level_match: str
    genre_match: str
    time_investment: int  # in minutes
    author_match: str
    assumptions: List[str]

class BookRecommendation(BaseModel):
    title: str
    author: str
    genre: str
    reading_level: str
    page_count: int
    estimated_time: int  # in minutes
    genre_match_percentage: float = Field(ge=0, le=100)
    plot_summary: str
    themes: List[str]
    writing_style: str

class RecommendationsResponse(BaseModel):
    recommendations: Annotated[List[BookRecommendation], Field(min_length=1, max_length=5)]
    fallback_explanations: Optional[List[str]] = None


class UserPreferences(BaseModel):
    favorite_genres: List[str]
    reading_level: str = Field(..., pattern="^(beginner|intermediate|advanced)$")
    preferred_authors: List[str]
    daily_reading_goal: int = Field(..., gt=0)

class StepByStepSolution(BaseModel):
    steps: List[str]
    final_answer: str
    confidence_score: Optional[float] = Field(None, ge=0, le=1)


class ReasoningStep(BaseModel):
    step_number: int = Field(..., gt=0)
    description: str
    reasoning_type: str = Field(..., pattern="^(logic|calculation|lookup|comparison)$")
    result: str

class CalculationResult(BaseModel):
    input_values: dict
    operation: str
    result: float
    units: Optional[str] = None
    confidence: float = Field(..., ge=0, le=1)

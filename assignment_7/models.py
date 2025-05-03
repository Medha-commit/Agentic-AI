from pydantic import BaseModel
from typing import List, Union

class BookAnalysisResponse(BaseModel):
    plot: str
    themes: List[str]
    writing_style: str
    recommendations: List[str]
    plot_summary: str
    reading_level_match: str
    genre_match: str
    time_investment: str
    author_match: str
    assumptions: Union[str, List[str]]  # Now accepts either string or list of strings

class BookRecommendation(BaseModel):
    title: str
    description: str

class RecommendationsResponse(BaseModel):
    recommendations: List[BookRecommendation]
    reasoning: str
    reading_level: str
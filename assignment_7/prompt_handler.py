from models import BookAnalysisResponse, RecommendationsResponse
from typing import List

class PromptHandler:
    @staticmethod
    def create_analysis_prompt(book_title: str, context: str) -> str:
        return f"""
        Given the following book: {book_title}
        
        Context from the book:
        {context}
        
        Please analyze the book following these aspects:
        1. Plot Analysis:
           - Main storyline
           - Key events
           - Character development
        2. Themes:
           - Major themes
           - Symbolism
           - Literary devices
        3. Writing Style:
           - Narrative technique
           - Language use
           - Structural elements
        4. Recommendations:
           - Similar books
           - Why recommended
           - Target audience
        
        Output must be in JSON format matching these fields:
        {
            "plot": "detailed plot summary",
            "themes": ["list of main themes"],
            "writing_style": "analysis of writing style",
            "recommendations": ["list of similar books"]
        }
        """

    @staticmethod
    def create_recommendation_prompt(preferences: dict, context: str) -> str:
        return f"""
        Given the following preferences: {preferences}
        
        Context from similar books:
        {context}
        
        Please provide recommendations that:
        1. Match user preferences
        2. Explain reasoning
        3. Consider reading level
        
        Output must be in JSON format matching these fields:
        {
            "recommendations": ["list of books"],
            "reasoning": "explanation for recommendations",
            "reading_level": "suggested reading level"
        }
        """
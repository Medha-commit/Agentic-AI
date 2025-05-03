import os
from dotenv import load_dotenv
import google.generativeai as genai
from rag_handler import RAGHandler
from models import BookAnalysisResponse, RecommendationsResponse
import json
import re

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class Perception:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        self.rag = RAGHandler()

    def analyze_book(self, book_title: str, content: str = None):
        if content:
            self.rag.add_book_content(book_title, content)
            relevant_passages = self.rag.retrieve_relevant_passages(book_title)
            context = "\n".join(relevant_passages)
        else:
            context = book_title

        response = self.model.generate_content(
            f"Analyze this book with context:\n{context}\n"
            "Provide a JSON object with exactly these fields (no nested objects):\n"
            "{\n"
            '  "plot": "detailed plot summary",\n'
            '  "themes": ["theme1", "theme2"],\n'
            '  "writing_style": "analysis of writing style",\n'
            '  "recommendations": ["book1", "book2"],\n'
            '  "plot_summary": "short summary",\n'
            '  "reading_level_match": "reading level",\n'
            '  "genre_match": "genre analysis",\n'
            '  "time_investment": "reading time estimate",\n'
            '  "author_match": "author style analysis",\n'
            '  "assumptions": "analysis assumptions"\n'
            "}\n"
            "Ensure all fields are present and properly formatted.",
            generation_config={"temperature": 0.7, "top_k": 40, "candidate_count": 1}
        )
        
        # Clean and parse response
        text = response.text
        # Remove markdown formatting if present
        text = re.sub(r'```json\s*|\s*```', '', text)
        # Parse JSON
        try:
            analysis_dict = json.loads(text)
            return BookAnalysisResponse(**analysis_dict)
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON: {text}")
            raise e

    def get_recommendations(self, preferences: dict):
        query = f"Find books similar to preferences: {preferences}"
        relevant_passages = self.rag.retrieve_relevant_passages(query)
        context = "\n".join(relevant_passages)
        
        response = self.model.generate_content(
            f"Based on these preferences and context:\n{context}\n"
            "Provide recommendations in JSON format (without markdown formatting) with these fields:\n"
            "- recommendations: list of book objects with 'title' and 'description' fields\n"
            "- reasoning: explanation for recommendations\n"
            "- reading_level: suggested reading level\n\n"
            "Example format:\n"
            '{\n'
            '  "recommendations": [\n'
            '    {"title": "Book Title", "description": "Why this book matches"}\n'
            '  ],\n'
            '  "reasoning": "Overall explanation",\n'
            '  "reading_level": "Advanced"\n'
            '}',
            generation_config={"temperature": 0.7, "top_k": 40, "candidate_count": 1}
        )
        
        # Clean and parse response
        text = response.text
        # Remove markdown formatting if present
        text = re.sub(r'```json\s*|\s*```', '', text)
        # Parse JSON
        try:
            recommendations_dict = json.loads(text)
            return RecommendationsResponse(**recommendations_dict)
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON: {text}")
            raise e

    def search_books(self, query: str) -> list:
        relevant_passages = self.rag.retrieve_relevant_passages(query)
        return relevant_passages
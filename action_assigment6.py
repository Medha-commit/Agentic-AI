from models import Book
from perception import Perception

class ActionExecutor:
    def __init__(self, memory):
        self.memory = memory
        self.perception = Perception()
    
    async def execute(self, action: str, params: dict):
        if action == "recommend_books":
            # Use LLM for intelligent recommendations based on preferences
            recommendations = await self.perception.get_recommendations(
                preferences=params.get('preferences', {})
            )
            return recommendations
            
        elif action == "analyze_book":
            return "Ready to analyze book"
            
        elif action == "add_book":
            # Optional: Keep the add functionality for user's personal library
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            rating = float(input("Enter rating (0-5): ") or "0")
            notes = input("Enter notes (optional): ")
            
            book = Book(
                title=title,
                author=author,
                genre=genre,
                rating=rating,
                notes=notes
            )
            self.memory.add_book(book)
            return f"Added book: {book.title}"
            
        return f"Unknown action: {action}"

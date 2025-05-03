import json
from models import Book

class ActionExecutor:
    def __init__(self, memory, perception):
        self.memory = memory
        self.perception = perception

    def execute(self, action_type: str, data: dict):
        if action_type == "add_book":
            title = input("Book title: ")
            author = input("Author: ")
            genre = input("Genre: ")
            rating = float(input("Rating (0-5): "))
            notes = input("Notes (optional): ")
            content = input("Book content or summary: ")
            minutes_read = int(input("Minutes spent reading: "))
            pages_read = int(input("Pages read: "))
            
            book = self.memory.add_book(
                title=title,
                author=author,
                genre=genre,
                content=content,
                rating=rating,
                notes=notes
            )
            self.memory.add_to_reading_history(title, pages_read, minutes_read)
            return "Book and reading progress added successfully"
            
        elif action_type == "analyze_book":
            title = input("Enter book title or query to analyze: ")
            book = next((b for b in self.memory.get_books() if b.title.lower() == title.lower()), None)
            analysis = self.perception.analyze_book(title, book.content if book else None)
            return f"Analysis: {analysis}"
            
        elif action_type == "get_recommendations":
            preferences = {
                "favorite_genres": input("Favorite genres (comma-separated): ").split(","),
                "reading_level": input("Reading level (beginner/intermediate/advanced): "),
                "preferred_authors": input("Preferred authors (comma-separated): ").split(","),
                "daily_reading_goal": int(input("Daily reading goal (minutes): "))
            }
            recommendations = self.perception.get_recommendations(preferences)
            return f"Recommendations: {recommendations}"
            
        elif action_type == "view_history":
            history = self.memory.get_reading_history()
            total_time = self.memory.get_total_reading_time()
            if not history:
                return "No reading history available yet"
            return f"Reading History:\n{json.dumps(history, indent=2)}\nTotal reading time: {total_time} minutes"
            
        elif action_type == "search_books":
            query = input("Enter search query: ")
            results = self.perception.search_books(query)
            return f"Search Results:\n{json.dumps(results, indent=2)}"
        
        else:
            raise ValueError(f"Unknown action type: {action_type}")
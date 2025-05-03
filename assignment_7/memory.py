from models import Book
from typing import List, Optional, Dict
from datetime import datetime
import json
import os

class Memory:
    def __init__(self):
        self.storage_file = "books_database.json"
        self.reading_history_file = "reading_history.json"
        self.books = self.load_books()
        self.reading_history = self.load_reading_history()

    def load_books(self) -> List[Book]:
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as f:
                books_data = json.load(f)
                return [Book(**book) for book in books_data]
        return []

    def save_books(self):
        books_data = [book.model_dump() for book in self.books]
        with open(self.storage_file, 'w') as f:
            json.dump(books_data, f, indent=2)

    def add_book(self, title: str, author: str, genre: str, content: str = None, 
                 rating: Optional[float] = None, notes: Optional[str] = None) -> Book:
        book = Book(
            title=title,
            author=author,
            genre=genre,
            content=content,
            rating=rating,
            notes=notes
        )
        self.books.append(book)
        self.save_books()
        return book

    def get_books(self) -> List[Book]:
        return self.books

    def load_reading_history(self) -> Dict:
        if os.path.exists(self.reading_history_file):
            with open(self.reading_history_file, 'r') as f:
                return json.load(f)
        return {}

    def save_reading_history(self):
        with open(self.reading_history_file, 'w') as f:
            json.dump(self.reading_history, f, indent=2)

    def add_to_reading_history(self, book_title: str, pages_read: int = 0, minutes_spent: int = 0):
        if book_title not in self.reading_history:
            self.reading_history[book_title] = []
        
        entry = {
            "date": datetime.now().isoformat(),
            "pages_read": pages_read,
            "minutes_spent": minutes_spent
        }
        self.reading_history[book_title].append(entry)
        self.save_reading_history()

    def get_reading_history(self, book_title: Optional[str] = None) -> Dict:
        if book_title:
            return {book_title: self.reading_history.get(book_title, [])}
        return self.reading_history

    def get_total_reading_time(self) -> int:
        total_minutes = 0
        for book in self.reading_history.values():
            for entry in book:
                total_minutes += entry["minutes_spent"]
        return total_minutes
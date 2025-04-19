import json
from models import Book

class Memory:
    def __init__(self):
        self.reading_list = []
        self.reading_history = []
        self.recommendations = []
    
    def add_book(self, book: Book):
        self.reading_list.append(book)
    
    def get_reading_list(self) -> list[Book]:
        return self.reading_list
    
    def save_to_file(self):
        with open('reading_list.json', 'w') as f:
            json.dump([book.dict() for book in self.reading_list], f)
    
    def load_from_file(self):
        try:
            with open('reading_list.json', 'r') as f:
                data = json.load(f)
                self.reading_list = [Book(**book) for book in data]
        except FileNotFoundError:
            self.reading_list = []

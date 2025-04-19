from models import Book

class DecisionMaker:
    def __init__(self):
        self.actions = {
            'add': 'add_book',
            '1': 'add_book',
            'analyze': 'analyze_book',
            '2': 'analyze_book',
            'recommend': 'recommend_books',
            '3': 'recommend_books'
        }
    
    def determine_action(self, user_input: str) -> dict:
        # Clean the input
        cleaned_input = user_input.lower().strip()
        
        # Get the action from the mapping
        action = self.actions.get(cleaned_input, 'unknown')
        
        return {
            "action": action,
            "params": {}
        }
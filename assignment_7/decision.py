class DecisionMaker:
    def __init__(self):
        self.actions = {
            'add': 'add_book',
            '1': 'add_book',
            'analyze': 'analyze_book',
            '2': 'analyze_book',
            'recommend': 'get_recommendations',
            '3': 'get_recommendations',
            'history': 'view_history',
            '4': 'view_history',
            'search': 'search_books',
            '5': 'search_books',
            'quit': 'quit',
            '6': 'quit'
        }
    
    def determine_action(self, user_input: str) -> dict:
        cleaned_input = user_input.lower().strip()
        action = self.actions.get(cleaned_input, 'unknown')
        
        return {
            "action": action,
            "params": {}
        }
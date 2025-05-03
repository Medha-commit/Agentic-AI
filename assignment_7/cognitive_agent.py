from memory import Memory
from perception import Perception
from action import ActionExecutor
from decision import DecisionMaker

class CognitiveAgent:
    def __init__(self):
        self.memory = Memory()
        self.perception = Perception()
        self.decision_maker = DecisionMaker()
        self.action_executor = ActionExecutor(self.memory, self.perception)

    def run(self):
        self.initialize()
        
        while True:
            print("\nAvailable actions:")
            print("1 or 'add' - Add a new book")
            print("2 or 'analyze' - Analyze a book")
            print("3 or 'recommend' - Get recommendations")
            print("4 or 'history' - View reading history")
            print("5 or 'search' - Search through books")
            print("6 or 'quit' - Exit the program")
            
            user_input = input("\nWhat would you like to do? ")
            if user_input.lower().strip() in ['6', 'quit']:
                break
            
            decision = self.decision_maker.determine_action(user_input)
            result = self.action_executor.execute(decision["action"], decision["params"])
            print(f"\nResult: {result}")

    def initialize(self):
        print("Successfully initialized reading assistant with RAG capabilities")

    def analyze_book_action(self, book_title: str, content: str = None):
        # Gets structured response using Pydantic model
        analysis: BookAnalysisResponse = self.perception.analyze_book(book_title, content)
        
        # Can now access structured data
        print(f"Plot: {analysis.plot}")
        print(f"Themes: {', '.join(analysis.themes)}")
        print(f"Writing Style: {analysis.writing_style}")
        print(f"Recommendations: {', '.join(analysis.recommendations)}")

    def get_recommendations_action(self, preferences: dict):
        # Gets structured response using Pydantic model
        recommendations: RecommendationsResponse = self.perception.get_recommendations(preferences)
        
        # Access structured data
        print(f"Recommended Books: {', '.join(recommendations.recommendations)}")
        print(f"Reasoning: {recommendations.reasoning}")
        print(f"Reading Level: {recommendations.reading_level}")
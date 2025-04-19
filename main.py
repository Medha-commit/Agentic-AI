import asyncio
from perception import Perception
from memory import Memory
from decision import DecisionMaker
from action import ActionExecutor
from models import UserPreferences, StepByStepSolution
from prompt_handler import PromptHandler

class CognitiveAgent:
    def __init__(self):
        self.perception = Perception()
        self.memory = Memory()
        self.decision = DecisionMaker()
        self.action = None
        self.user_preferences = None

    async def initialize(self):
        # Get user preferences
        self.user_preferences = UserPreferences(
            favorite_genres=input("Favorite genres (comma-separated): ").split(','),
            reading_level=input("Reading level (beginner/intermediate/advanced): "),
            preferred_authors=input("Preferred authors (comma-separated): ").split(','),
            daily_reading_goal=int(input("Daily reading goal (minutes): "))
        )
        self.action = ActionExecutor(self.memory)

    async def run(self):
        await self.initialize()
        
        while True:
            print("\nAvailable actions:")
            print("1 or 'add' - Add a new book")
            print("2 or 'analyze' - Analyze a book")
            print("3 or 'recommend' - Get recommendations")
            print("4 or 'quit' - Exit the program")
            
            user_input = input("\nWhat would you like to do? ")
            if user_input.lower().strip() in ['4', 'quit']:
                break
                
            # Decision making
            decision_result = self.decision.determine_action(user_input)
            
            try:
                # Action execution
                # In the run method, update the action execution:
                result = await self.action.execute(
                    decision_result["action"], 
                    {"preferences": self.user_preferences.model_dump()}
                )
                
                # Perception analysis if needed
                if decision_result["action"] == "analyze_book":
                    book_info = input("Enter book title or query to analyze: ")
                    analysis = await self.perception.analyze_book(
                        book_info, 
                        self.user_preferences.model_dump()
                    )
                    print(f"\nAnalysis: {analysis}")
                
                print(f"\nResult: {result}")
            except Exception as e:
                print(f"\nError: {str(e)}")

async def main():
    agent = CognitiveAgent()
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())
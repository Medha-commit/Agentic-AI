from models import ReasoningStep, CalculationResult, StepByStepSolution
from typing import List

class PromptHandler:
    @staticmethod
    def create_structured_prompt(query: str, user_prefs: dict) -> str:
        return f"""
        Given the following calculation request: {query}
        
        User Preferences:
        - Operations: {', '.join(user_prefs['preferred_operations'])}
        - Complexity: {user_prefs['complexity_level']}
        - Verification: {user_prefs['verification_required']}
        
        Please follow these steps:
        1. Break down the problem into logical steps
        2. For each step:
           - Identify the reasoning type (arithmetic/logic/tool_use/verification)
           - Describe the step
           - Assign a confidence level
           - Indicate if verification is needed
        3. Show calculations with input values and results
        4. Verify intermediate results
        5. Provide a final answer with confidence level
        
        If uncertain at any step:
        - Mark it for human verification
        - Explain the uncertainty
        - Suggest alternative approaches
        
        Output must be in this format:
        REASONING_STEPS: [list of steps with type and description]
        CALCULATIONS: [list of calculations with inputs and results]
        FINAL_ANSWER: [result with confidence level]
        """

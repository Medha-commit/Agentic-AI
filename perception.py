import google.generativeai as genai
import os
from dotenv import load_dotenv
from models import BookAnalysisRequest, BookAnalysisResponse, RecommendationsResponse, BookRecommendation

class Perception:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in .env file")
            
        # Initialize Gemini with flash model
        genai.configure(api_key=api_key)
        model_name = 'gemini-2.0-flash'
        try:
            self.model = genai.GenerativeModel(model_name)
            print(f"Successfully initialized {model_name}")
        except Exception as e:
            print(f"Error initializing model: {e}")
            raise
    
    async def analyze_book(self, book_info: str, preferences: dict) -> BookAnalysisResponse:
        request = BookAnalysisRequest(book_info=book_info, preferences=preferences)
        try:
            prompt = f"""You are a helpful Reading Assistant.

Your task is to analyze a book and recommend similar books based on user preferences. Follow these steps carefully and provide structured, validated, and thoughtful responses.

### User Preferences:
- Favorite Genres: {preferences.get('favorite_genres', [])}
- Reading Level: {preferences.get('reading_level', '')}
- Preferred Authors: {preferences.get('preferred_authors', [])}
- Daily Reading Goal: {preferences.get('daily_reading_goal', 0)} minutes

### Book to Analyze:
"{book_info}"

### Instructions:
1. **Step-by-Step Reasoning**
   - Think out loud before giving your final answer.
   - For each analysis section, explain how you reached the conclusion.
   - Use reasoning such as genre identification, complexity comparison, and author similarity.

2. **Book Analysis (Use Headings)**
   - **Plot Summary and Key Themes**  
     Summarize the book and highlight 2–3 major themes.
   
   - **Writing Style and Complexity Level**  
     Evaluate the tone, structure, and match with the user's reading level.

   - **Genre Suitability and Reader Fit**  
     Check if the book aligns with preferred genres. If not, explain why it may still be a good fit.

   - **Time Investment Estimation**  
     Estimate reading time based on average page count and user's daily goal. Explain your calculation.

   - **Author Match or Similarity**  
     Check if the author is among the preferred list. If not, suggest why they might still be interesting (style, genre, themes).

3. **Self-Check**  
   - After completing your analysis, list 1–2 assumptions you made and briefly validate them.

4. **Fallback Handling**
   - If you cannot find an exact match to any preference, offer the closest match and justify your selection.
   - Clearly state when something is unknown or assumed.

5. **Output Format (Use Markdown with Bullet Points)**
   - Use headings for each section.
   - Use bullet points or short paragraphs for clarity.
   - Keep the tone friendly and informative.

Provide your analysis now."""
            
            response = self.model.generate_content(prompt)
            # Parse the response into structured format
            parsed_response = self._parse_analysis_response(response.text)
            return BookAnalysisResponse(**parsed_response)
        except Exception as e:
            raise ValueError(f"Analysis error: {str(e)}")

    async def get_recommendations(self, preferences: dict) -> RecommendationsResponse:
        try:
            prompt = f"""You are a helpful Reading Assistant.

### User Preferences:
- Favorite Genres: {preferences.get('favorite_genres', [])}
- Reading Level: {preferences.get('reading_level', '')}
- Preferred Authors: {preferences.get('preferred_authors', [])}
- Daily Reading Goal: {preferences.get('daily_reading_goal', 0)} minutes

### Instructions:
1. **Step-by-Step Reasoning Process**
   - First, analyze the user's preferences
   - Then, identify potential book matches
   - Finally, validate each recommendation against preferences
   - Tag your reasoning with [genre], [level], [author], or [time] as appropriate

2. **Recommendation Structure**
   For each recommended book (provide 5 books):
   - **Book Details**
     * Title and Author
     * Genre and Reading Level
     * Page Count and Estimated Reading Time

   - **Preference Matching**
     * Genre alignment explanation
     * Reading level suitability
     * Author connection (direct or similar style)
     * Time investment calculation

   - **Content Overview**
     * Plot summary
     * Key themes
     * Writing style analysis

3. **Self-Verification Steps**
   After each recommendation:
   - Verify genre match percentage
   - Confirm reading level appropriateness
   - Validate time commitment against daily goal
   - Note any assumptions made

4. **Fallback Handling**
   If a perfect match isn't found:
   - Explain why the recommendation is still valuable
   - Highlight alternative matching criteria
   - Suggest adaptation strategies

5. **Output Format**
   - Use clear headings and bullet points
   - Include reasoning tags where appropriate
   - Maintain consistent structure across recommendations

Begin your recommendations now, ensuring each follows this structured format."""
            
            response = self.model.generate_content(prompt)
            # Parse the response into structured format
            parsed_response = self._parse_recommendations_response(response.text)
            return RecommendationsResponse(**parsed_response)
        except Exception as e:
            raise ValueError(f"Recommendation error: {str(e)}")

    def _parse_analysis_response(self, text: str) -> dict:
        try:
            # Default values in case parsing fails
            parsed = {
                "plot_summary": "",
                "themes": [],
                "writing_style": "",
                "reading_level_match": "",
                "genre_match": "",
                "time_investment": 0,
                "author_match": "",
                "assumptions": []
            }
            
            # Basic parsing logic - can be enhanced for better accuracy
            sections = text.split("##")
            for section in sections:
                if "Plot Summary" in section:
                    parsed["plot_summary"] = section.split("\n", 1)[1].strip()
                elif "Themes" in section:
                    themes_text = section.split("\n", 1)[1].strip()
                    parsed["themes"] = [t.strip("- ") for t in themes_text.split("\n") if t.strip()]
                elif "Writing Style" in section:
                    parsed["writing_style"] = section.split("\n", 1)[1].strip()
                elif "Genre Suitability" in section:
                    parsed["genre_match"] = section.split("\n", 1)[1].strip()
                elif "Time Investment" in section:
                    # Extract just the number of minutes
                    time_text = section.split("\n", 1)[1].strip()
                    import re
                    if minutes := re.search(r'(\d+)\s*minutes', time_text):
                        parsed["time_investment"] = int(minutes.group(1))
                elif "Author Match" in section:
                    parsed["author_match"] = section.split("\n", 1)[1].strip()
                elif "Self-Check" in section or "Assumptions" in section:
                    assumptions_text = section.split("\n", 1)[1].strip()
                    parsed["assumptions"] = [a.strip("- ") for a in assumptions_text.split("\n") if a.strip()]
            
            return parsed
            
        except Exception as e:
            raise ValueError(f"Failed to parse analysis response: {str(e)}")

    def _parse_recommendations_response(self, text: str) -> dict:
        try:
            recommendations = []
            fallback_explanations = []
            current_book = {}
            
            sections = text.split("##")
            for section in sections:
                if "Book Details" in section:
                    if current_book:  # Save previous book if exists
                        recommendations.append(current_book)
                    current_book = {
                        "title": "",
                        "author": "",
                        "genre": "",
                        "reading_level": "",
                        "page_count": 0,
                        "estimated_time": 0,
                        "genre_match_percentage": 0.0,
                        "plot_summary": "",
                        "themes": [],
                        "writing_style": ""
                    }
                    
                    lines = section.split("\n")
                    for line in lines:
                        if "Title" in line:
                            current_book["title"] = line.split(":", 1)[1].strip()
                        elif "Author" in line:
                            current_book["author"] = line.split(":", 1)[1].strip()
                        elif "Genre" in line:
                            current_book["genre"] = line.split(":", 1)[1].strip()
                        elif "Reading Level" in line:
                            current_book["reading_level"] = line.split(":", 1)[1].strip()
                        elif "Page Count" in line:
                            import re
                            if pages := re.search(r'(\d+)', line):
                                current_book["page_count"] = int(pages.group(1))
                        elif "Time" in line:
                            if time := re.search(r'(\d+)', line):
                                current_book["estimated_time"] = int(time.group(1))
                
                elif "Preference Matching" in section:
                    if "genre match" in section.lower():
                        import re
                        if match := re.search(r'(\d+)%', section):
                            current_book["genre_match_percentage"] = float(match.group(1))
                
                elif "Content Overview" in section:
                    lines = section.split("\n")
                    for i, line in enumerate(lines):
                        if "Plot summary" in line:
                            current_book["plot_summary"] = lines[i+1].strip("- ").strip()
                        elif "Key themes" in line:
                            themes = []
                            j = i + 1
                            while j < len(lines) and lines[j].strip().startswith("-"):
                                themes.append(lines[j].strip("- ").strip())
                                j += 1
                            current_book["themes"] = themes
                        elif "Writing style" in line:
                            current_book["writing_style"] = lines[i+1].strip("- ").strip()
                
                elif "Fallback" in section:
                    fallbacks = [line.strip("- ").strip() 
                               for line in section.split("\n") 
                               if line.strip().startswith("-")]
                    if fallbacks:
                        fallback_explanations.extend(fallbacks)

            # Add the last book if exists
            if current_book:
                recommendations.append(current_book)

            return {
                "recommendations": recommendations[:5],  # Ensure max 5 recommendations
                "fallback_explanations": fallback_explanations
            }
            
        except Exception as e:
            raise ValueError(f"Failed to parse recommendations response: {str(e)}\nText: {text[:200]}...")
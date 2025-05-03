from perception import Perception
from rag_handler import RAGHandler

def test_rag():
    perception = Perception()
    
    # 1. Add a book to the vector database
    book_title = "The Great Gatsby"
    book_content = """
    The Great Gatsby is a 1925 novel by F. Scott Fitzgerald. Set in the Jazz Age on Long Island, 
    the novel depicts narrator Nick Carraway's interactions with mysterious millionaire Jay Gatsby 
    and Gatsby's obsession to reunite with his former lover, Daisy Buchanan.
    The story explores themes of decadence, idealism, social upheaval, and excess, 
    creating a portrait of the Jazz Age that has been described as a cautionary tale about the American Dream.
    """
    print("\n1. Adding book to vector database...")
    analysis = perception.analyze_book(book_title, book_content)
    print(f"Book Analysis: {analysis}")

    # 2. Test semantic search
    print("\n2. Testing semantic search...")
    search_query = "books about wealth and american dream"
    results = perception.search_books(search_query)
    print(f"Search Results: {results}")

    # 3. Test recommendations
    print("\n3. Testing recommendations...")
    preferences = {
        "favorite_genres": ["literary fiction"],
        "reading_level": "advanced",
        "preferred_themes": ["social commentary", "wealth inequality"]
    }
    recommendations = perception.get_recommendations(preferences)
    print(f"Recommendations: {recommendations}")

if __name__ == "__main__":
    test_rag()
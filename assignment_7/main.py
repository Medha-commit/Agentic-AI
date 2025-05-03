from perception import Perception

def main():
    perception = Perception()
    
    # Add multiple books to build a better recommendation system
    books = {
        "The Great Gatsby": """
        The Great Gatsby is a 1925 novel by F. Scott Fitzgerald. Set in the Jazz Age on Long Island, 
        the novel depicts narrator Nick Carraway's interactions with mysterious millionaire Jay Gatsby 
        and Gatsby's obsession to reunite with his former lover, Daisy Buchanan.
        The story explores themes of decadence, idealism, social upheaval, and excess, 
        creating a portrait of the Jazz Age that has been described as a cautionary tale about the American Dream.
        """,
        
        "Pride and Prejudice": """
        Pride and Prejudice is a romantic novel by Jane Austen. The story follows Elizabeth Bennet 
        as she deals with issues of manners, upbringing, morality, education, and marriage in the landed 
        gentry of British Regency. The story's humor lies in its honest depiction of manners, education, 
        marriage and money in the British Regency period.
        """,
        
        "1984": """
        1984 is a dystopian novel by George Orwell. The story takes place in an imagined future where 
        most of the world has fallen victim to perpetual war, omnipresent government surveillance, historical 
        negationism, and propaganda. The novel examines the role of truth and facts within politics and the 
        ways in which they are manipulated.
        """
    }
    
    # Add books to the system
    for title, content in books.items():
        print(f"\nAnalyzing {title}...")
        analysis = perception.analyze_book(title, content)
        print(f"Analysis complete: {analysis}")
    
    # Test semantic search with specific calculation request
    print("\n2. Testing semantic search...")
    search_query = "books about wealth and american dream"
    results = perception.search_books(search_query)
    print(f"Search Results: {results}")
    
    # Get recommendations with structured preferences
    print("\nGetting recommendations...")
    user_preferences = {
        "preferred_operations": ["thematic_analysis", "genre_matching"],
        "complexity_level": "advanced",
        "verification_required": True
    }
    
    recommendations = perception.get_recommendations(user_preferences)
    print(f"Recommended books: {recommendations}")

if __name__ == "__main__":
    main()
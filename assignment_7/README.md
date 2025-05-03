# AI Book Recommendation System with RAG

A sophisticated book recommendation system that uses Retrieval-Augmented Generation (RAG) to provide intelligent, context-aware book recommendations.

## 🌟 Features

### Core Functionality
- **Smart Book Analysis**: Analyzes book content using RAG technology
- **Theme Extraction**: Identifies key themes and patterns in books
- **Contextual Recommendations**: Provides recommendations based on semantic understanding
- **Vector-Based Search**: Uses FAISS for efficient similarity search

### Technical Components
- **RAG Handler**: Manages document retrieval and context augmentation
- **Perception Module**: Processes and understands user queries
- **Gemini Integration**: Leverages Google's Gemini model for enhanced responses

## 🛠️ Architecture

```plaintext
assignment_7/
├── main.py           # Application entry point
├── perception.py     # Input processing and understanding
├── rag_handler.py    # RAG implementation
└── models.py         # Data models and structures
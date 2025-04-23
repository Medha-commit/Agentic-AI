# AI Reading Assistant

An intelligent reading assistant that helps users analyze books and get personalized recommendations using Google's Gemini AI.


## Project Structure

```python
assignment_6/
├── main.py              # Main application entry point
├── models.py            # Pydantic data models
├── action.py            # Action execution layer
├── decision.py          # Decision making layer
├── memory.py            # Data persistence layer
├── perception.py        # AI interaction layer
├── prompt_handler.py    # Prompt management
├── books_database.json  # Book storage
├── reading_history.json # Reading history storage
├── requirements.txt     # Project dependencies
└── .env                 # Environment variables (not in repo)

## Features

- **Book Analysis**: Detailed analysis of books including:
  - Plot summaries and key themes
  - Writing style evaluation
  - Reading level assessment
  - Time investment estimation
  - Genre and author matching

- **Smart Recommendations**: Get personalized book recommendations based on:
  - Favorite genres
  - Reading level
  - Preferred authors
  - Daily reading goals

- **Memory System**: Keep track of:
  - Books you've read
  - Personal ratings and notes
  - Reading preferences

## Getting Started

### Prerequisites

- Python 3.8+
- Google API Key for Gemini AI

### Installation

1. Clone the repository
```bash
git clone https://github.com/Medha-commit/Agentic-AI.git

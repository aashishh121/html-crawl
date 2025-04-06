# Website Content Search App
<div align="center"> <img src="https://github.com/aashishh121/html-crawl/blob/master/Screenshot%202025-04-06%20130640.png" alt="Website Content Search Screenshot" width="600"/> </div>

    A Single Page Application (SPA) that allows users to input a website URL and a search query,
    fetches the HTML content from the URL, splits it into tokenized chunks,
    indexes them into a vector database, and returns the Top 10 most relevant matches based on semantic search.

# Setup Instructions

    Clone this repository and navigate to the project directory:
    Run below command in terminal
    1. For frontend
        npm install
        npm run start

    2.For backend
        pip install -r requirements.txt
        docker-compose up -d
        python -m uvicorn main:app

        Ensure that Docker Desktop is running in the background.

The frontend application will be available at http://localhost:3000.

# Important Notes:

    In docker-compose.yml, the vector database uses the image:
      image: semitechnologies/transformers-inference:sentence-transformers-all-MiniLM-L6-v2
    You can choose a lighter model if needed for faster setup:
      image: semitechnologies/transformers-inference:sentence-transformers-all-MiniLM-L3-v2


# Tech Stack and Task Overview

    Frontend:
      React.js
      TailwindCSS

      Key Features:
        Two inputs:
          - Website URL field.
          - Search Query field.
        Submit Button - Triggers API request to backend.
        Displays results as responsive cards:
        - Shows content chunk, matching percentage, and option to view raw HTML.

    Backend:
        FastAPI
        BeautifulSoup4 (for HTML parsing)
        NLTK (for tokenization)
        Weaviate (for vector search)

      Core Functionality
        Fetch HTML: Request and download the raw HTML from the provided URL.
        Parse HTML: Clean and extract meaningful text using BeautifulSoup (remove <script>, <style>, etc.).
        Tokenize Content: Split text into chunks using NLTK tokenizer.
        Semantic Search: Embed the chunks and query, then search for top matches using Weaviate.

      API Endpoints:
        http://127.0.0.1:8000/api/v1/search (for search)

      Vector Database:
        Database Used: Weaviate (via Docker).
        Stored all chunk embeddings inside the vector database.
        Converted user query to an embedding.
        Queried the database to find the top 10 most relevant matches.

# Challenges & Improvements

    Challenges Faced:
      Handling HTML documents efficiently.
      Tokenizing and splitting chunks without cutting off semantic meaning.
      Vector database tuning for better semantic relevance.

    Potential Improvements:
      Pagination and infinite scroll on frontend.
      Caching previous search results for faster response.

# Need Help?

For any issues, feel free to create an issue in the repository or reach out to aashishkumargh@gmail.com.

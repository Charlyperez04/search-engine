# Seth's Blog Search

This project is a simple blog search application that allows users to search for blog posts from Seth Godin's collection. The application uses a dataset of Seth Godin's blog posts and leverages machine learning embeddings to provide relevant search results based on user input.

## Features

- **Search functionality**: Users can search for blog posts by entering keywords or topics.
- **Results display**: Displays the most relevant blog posts, including title, snippet, and a link to the full post.
- **Machine Learning**: Utilizes pre-trained embeddings to enhance the search accuracy and relevance of the results.

## How It Works

1. **Dataset**: The application uses a dataset of Seth Godin's blog posts, which includes the post titles, URLs, and content.
2. **Embeddings**: To provide an efficient search experience, the system uses embeddings generated from the content of the blog posts. These embeddings allow the search to understand the meaning behind the words and return relevant results.
3. **Search Process**: When a user inputs a query, the application compares the query to the embeddings and returns the most relevant blog posts.

## Technologies Used

- **Python**: The backend logic of the application is written in Python.
- **Streamlit**: A simple and interactive frontend to display the search interface and results.
- **txtai**: A machine learning library used to handle embeddings and perform the search.
- **Kaggle Hub**: Used to download the dataset containing Seth Godin's blog posts.

## Setup Instructions
1. Clone the repository:
    ```bash
    git clone https://github.com/Charlyperez04/search-engine.git
    ```

2. Navigate to the project directory:
    ```bash
    cd search-engine
    ```

3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    On Windows:
    ```bash
    venv\Scripts\activate
    ```

    On Mac/Linux:
    ```bash
    source venv/bin/activate
    ```

5. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. Run the Streamlit application:
    ```bash
    streamlit run main_streamlit.py
    ```

7. Open your browser and go to `http://localhost:8501` to start using the search tool.

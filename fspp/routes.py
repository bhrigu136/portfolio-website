from flask import render_template
from fspp import app

# --- CENTRALIZED PROJECT DATA ---
projects_data = [
    {
        'id': 1,
        'title': 'Credit Scoring using Random Forest',
        'description': 'Built a machine learning classification model to predict customer credit risk (good/bad) using the German Credit dataset. Implemented data preprocessing, handling of imbalanced data, and model evaluation.',
        'github': 'https://github.com/bhrigu136/Credit-Scoring-using-Random-Forest',
        'live': 'https://credit-scoring-using-random-forest-y4swxuubrbctwhjx6jxwte.streamlit.app/',
        'has_detail': False
    },
    {
        'id': 2,
        'title': 'House Price Prediction',
        'description': 'Developed a regression-based machine learning model to predict house prices using real-world housing data. Focused on feature engineering, data cleaning, and model performance evaluation.',
        'github': 'https://github.com/bhrigu136/House-Price-Prediction',
        'live': 'https://house-price-prediction-dzypzeofxzpdrl7wtp8ies.streamlit.app/',
        'has_detail': False
    },
        {
        'id': 3,
        'title': 'Movie Recommender System',
        'description': 'A content-based movie recommendation system built using machine learning techniques. Users receive personalized movie suggestions based on similarity measures.',
        'github': 'https://github.com/bhrigu136/movie-recommender-system',
        'live': 'https://movie-recommender-system-527ydffaajaykatymnjsl8.streamlit.app/',
        'has_detail': False
    },
    {
        'id': 4,
        'title': 'Flask ToDo App',
        'description': 'A full-stack Flask-based ToDo application with CRUD functionality, demonstrating backend development, routing, and database integration.',
        'github': 'https://github.com/bhrigu136/Flask-ToDo-App',
        'live': 'https://flask-todo-app-9fms.onrender.com/',
        'has_detail': False
    }

]

@app.route("/")
def home():
    # Show only top projects on home
    return render_template('index.html', projects=projects_data[:3])

@app.route("/projects")
def projects():
    return render_template('projects.html', projects=projects_data)

@app.route("/experience")
def experience():
    return render_template('experience.html')



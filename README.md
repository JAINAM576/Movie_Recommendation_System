# 🎬 Movie Recommendation System

## 📌 Project Overview
This is a **Content-Based Movie Recommendation System** built using **Python, Streamlit, and Machine Learning**. Users can search for a movie, and the system suggests similar movies based on **overview, genres, director, and cast**. 

## 📂 Directory Structure
```
├── jainam576-movie_recommendation_system/
│   ├── app.py                   # Streamlit App for User Interface
│   ├── requirements.txt         # Required dependencies
│   ├── template.py              # Project structure template
│   ├── Processed_Data/
│   │   └── TMDB_MOVIE_SUBDATASET.csv  # Processed movie dataset
│   ├── model_helpers/
│   │   ├── movie_metadata.pkl   # Movie metadata (Pandas DataFrame with 26820 movies)
│   │   └── similarity.pkl       # Similarity matrix (26820x50) for recommendations
│   └── research/
│       └── trail.ipynb          # Jupyter notebook with full preprocessing & model logic
```

## 🚀 Features
✅ **Search any movie** and get top **5 similar movies**
✅ **Optimized recommendation** using a **26820x50 similarity matrix**
✅ **Movie details**: poster, genres, and overview
✅ **User-friendly Streamlit interface**
✅ **Preprocessed data for efficiency**

## 🔧 Data Preprocessing & Model Development
1. **Dataset:** Used **TMDB Movies Dataset** from [Kaggle](https://www.kaggle.com/datasets/alanvourch/tmdb-movies-daily-updates/data).
2. **Preprocessing:**
   - Removed null values and unnecessary columns
   - Used **overview, genres, director, and cast** for similarity calculation
   - Combined these columns into a **single text paragraph** per movie
   - Applied **NLTK PorterStemmer** for text normalization
3. **Feature Engineering:**
   - Used **CountVectorizer (max_features=5000)** to create a **26820x5000 matrix**
   - Computed **cosine similarity** to measure movie relevance
   - Optimized storage by keeping **only top 50 similar movies per movie (26820x50 matrix)**
4. **Model Storage:**
   - Stored **movie metadata (26820x27)** and **similarity matrix (26820x50)** using `joblib`

## 🎨 Streamlit App (`app.py`)
- Users enter a movie name and receive **recommendations with movie posters**.
- The app fetches movie posters using:
  ```python
  poster_url = "https://image.tmdb.org/t/p/original/" + movie_df["poster_path"]
  ```
- The UI is interactive with a **slider for the number of recommendations**.

## 📦 Installation & Setup
### 1️⃣ Clone the repository
```sh
git clone https://github.com/yourusername/jainam576-movie_recommendation_system.git
cd jainam576-movie_recommendation_system
```
### 2️⃣ Create a Virtual Environment (Python 3.12)
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```
### 3️⃣ Install dependencies
```sh
pip install -r requirements.txt
```
### 4️⃣ Run the Streamlit App
```sh
streamlit run app.py
```

## 🔥 Future Improvements
- Enhance similarity calculation using **TF-IDF or BERT embeddings**
- Add **collaborative filtering (user-based recommendations)**
- Improve **UI with better visualization and filters**

## 📜 License
This project is open-source and available under the **MIT License**.

---
💡 **Developed by [Jainam Sanghavi]** | ✉️ Contact: [sanghavijainam86@gmail.com]

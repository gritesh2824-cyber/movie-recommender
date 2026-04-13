# 🎬 Movie Recommender System

A content-based Movie Recommender System built using **Python**, **Streamlit**, and the **TMDB API**.
It suggests movies similar to the one selected by the user and displays their posters.

---

## 🚀 Features

* 🎯 Recommend top 5 similar movies
* 🖼️ Fetch movie posters using TMDB API
* 🎨 Beautiful UI with Streamlit
* ⚡ Fast and interactive
* 🔐 Secure API key using environment variables

---

## 🛠️ Tech Stack

* Python 🐍
* Streamlit
* Pandas
* Scikit-learn
* TMDB API

---

## 📂 Project Structure

```
movie-recommender/
│── app.py
│── movie_dict.pkl
│── .gitignore
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
```

---

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Add TMDB API Key

Create a `.env` file in the root directory:

```
TMDB_API_KEY=your_api_key_here
```

---

### 4️⃣ Run the app

```
streamlit run app.py
```

---

## 🌐 Deployment

You can deploy this app easily on:

* Streamlit Cloud (Recommended)
* Render
* Heroku

---

## 🧠 How It Works

* Movie data is processed using NLP techniques
* Text features are converted into vectors
* Cosine similarity is used to find similar movies
* TMDB API is used to fetch posters

---

## ⚠️ Note

* Large files like `similarity.pkl` are excluded using `.gitignore`
* Similarity is computed dynamically for better scalability

---

## 📸 Demo

(Add screenshots here after deployment)

---

## 🤝 Contributing

Feel free to fork this repo and improve the project!

---

## 📜 License

This project is for educational purposes only.

---

## 👨‍💻 Author

Ritesh Gupta

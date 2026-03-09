# 📧 SMS Spam Classifier

A Machine Learning web application that classifies SMS messages as **Spam** or **Not Spam (Ham)** using Natural Language Processing (NLP).
The app is built with **Python**, **Scikit-learn**, **NLTK**, and **Streamlit**.

---

## 🚀 Live Demo

https://sms-spam-classifier-afrd8ceddaph5ryp93hdz2.streamlit.app/

---

## 📌 Features

* Detects whether a message is **Spam** or **Not Spam**
* Text preprocessing using **NLTK**
* Stopword removal and stemming
* Vectorization using **CountVectorizer**
* Machine learning model for prediction
* Interactive web interface built with **Streamlit**

---

## 🧠 Machine Learning Pipeline

1. User enters a message
2. Text preprocessing

   * Lowercasing
   * Tokenization
   * Stopword removal
   * Stemming
3. Convert text to numerical features using **CountVectorizer**
4. Pass vectorized text to the trained model
5. Model predicts:

   * **Spam**
   * **Not Spam**

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Scikit-learn
* NLTK
* NumPy
* Pandas

---

## 📂 Project Structure

```
sms-spam-classifier
│
├── app.py
├── model.pkl
├── count_vectorizer.pkl
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/sms-spam-classifier.git
cd sms-spam-classifier
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

The app will open in your browser.

---

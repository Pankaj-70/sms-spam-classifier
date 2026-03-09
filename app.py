import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import streamlit as st
import string
nltk.download('punkt_tab')
nltk.download('stopwords')

prt = PorterStemmer()
model = pickle.load(open('model.pkl', 'rb'))
cv = pickle.load(open('count_vectorizer.pkl', 'rb'))

def transform_text(text):
    #lower
    text = text.lower()
    res = []
    text = nltk.word_tokenize(text);
    for i in text:
        #special character 
        if i.isalnum():
            #stopwords and punctuation
            if i not in stopwords.words('english') and i not in string.punctuation:
                #stemming
                res.append(prt.stem(i))
    
    return (" ").join(res)




st.title("SMS spam classifier")
sms = st.text_area("Enter the message")
if st.button('Predict'):
    #preprocess
    transformed_txt = transform_text(sms)
    #vectorize
    vectorized_val = cv.transform([transformed_txt])
    #prediction
    res = model.predict(vectorized_val)[0]
    if res == 1:
        st.header("Spam")
    else:
        st.header("Not spam")


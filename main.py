import os
import nltk
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import json

ssl._create_default_https_content = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')

# Load intents from intents.json file
with open('intents.json', 'r', encoding = 'utf-8') as file:
    data = json.load(file)

# Extract intents
intents = data['intents']


# Create Vectorizer and Classifier
vectorizer = TfidfVectorizer()
classifier = LogisticRegression(random_state=0, max_iter=1000)

# Preprocess the data
tags = []
patterns = []
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)   
        
# Training the model
X = vectorizer.fit_transform(patterns)
y = tags
classifier.fit(X, y)

# Create Chatbot
def chatbot(input_text):
    input_text = vectorizer.transform([input_text])
    tag = classifier.predict(input_text)[0]
    for intent in intents:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            return response
        
# Chabot with StreamLit
counter = 0
def main():
    
    st.markdown(
        """
        <style>
        body {
            background-image: url('https://source.unsplash.com/random/1600x900'); /
            background-size: cover;
            font-family: 'Roboto', sans-serif; 
            color: #333;
        }
        .main {
            background-color: rgba(240, 242, 246, 0.9); 
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            max-width: 800px;
            margin: auto;
        }
        .chat-bubble-user {
            background-color: #DCF8C6;
            border-radius: 10px;
            padding: 10px;
            margin: 10px;
            width: fit-content;
            max-width: 70%;
            align-self: flex-end;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .chat-bubble-bot {
            background-color: #FFFFFF;
            border-radius: 10px;
            padding: 10px;
            margin: 10px;
            width: fit-content;
            max-width: 70%;
            align-self: flex-start;
            border: 1px solid #ccc;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .chat-container {
            display: flex;
            flex-direction: column;
            margin-top: 20px;
        }
        .stTextInput>div>input {
            border-radius: 20px;
            padding: 10px;
            border: 1px solid #ddd;
        }
        .stTextInput>div>input:focus {
            outline: none;
            border-color: #007bff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    global counter 
    st.title("💬 Chatbot with Streamlit")
    st.write("Welcome! Start chatting with the bot below. Type a message and press Enter.")
    
    if 'conversation' not in st.session_state:
        st.session_state.conversation = []
    
    counter += 1
    user_input = st.text_input("You:", key = f"user_input_{counter}", placeholder = "Type your message...")
    
    if user_input:
        response = chatbot(user_input)
        st.text_area("Chatbot:", value = response, height = 100, max_chars = None, key = f"chatbot_response_{counter}")
        
        if response.lower() in ["goodbye", "bye"]:
            st.write("Thanks")
            st.stop()
            
            
    # Display the conversation
    chat_container = st.container()
    with chat_container:
        for chat in st.session_state.conversation:
            st.markdown(
                f'<div class="chat-container">'
                f'<div class="chat-bubble-user">{chat["user"]}</div>'
                f'<div class="chat-bubble-bot">{chat["bot"]}</div>'
                f'</div>',
                unsafe_allow_html=True
            )


if __name__ == "__main__":
    main()    
# 🤖 Streamlit Chatbot

Welcome to the **Streamlit Chatbot**! 🚀 This project features a chatbot built using Streamlit and Python. The chatbot leverages machine learning to interact with users and provide responses based on predefined intents.

## 📦 Features

- **Chat Interface**: Engaging user interface with real-time conversation capabilities.
- **Machine Learning**: Utilizes TF-IDF Vectorizer and Logistic Regression for intent classification.
- **Easy Deployment**: Simple to run locally with Streamlit or deploy on the cloud.
- **Customizable**: Easily update intents and responses in `intents.json`.

## 🚀 Getting Started


### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Kheav-Kienghok/streamlit-chatbot

2. **Navigate into the project directory::**
   
   ```bash
   cd streamlit-chatbot

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt

3. **Run the Streamlit app:**

    ```bash
    streamlit run main.py

## 💡 How It Works

### 1. Data Preparation
- **Intents**: The chatbot's responses are based on predefined intents stored in the `intents.json` file. This file contains various user queries and the corresponding responses. Each intent includes:
  - `tag`: A label for the intent (e.g., "greeting").
  - `patterns`: A list of user inputs that match this intent (e.g., "Hello", "Hi there").
  - `responses`: A list of possible responses the chatbot can give for this intent (e.g., "Hello! How can I help you today?").

### 2. Training
- **Vectorization**: The chatbot uses the TF-IDF (Term Frequency-Inverse Document Frequency) Vectorizer to convert text data into numerical vectors. This helps in understanding the importance of words in the context of user inputs.
- **Classification**: A Logistic Regression model is trained using the vectorized data. The model learns to classify user inputs into predefined intents based on their similarity to the training data.

### 3. Chat Interface
- **Streamlit App**: The Streamlit framework provides an interactive web-based interface for the chatbot. Users can type their messages into a text input field.
- **Response Generation**: When a user sends a message, the chatbot processes the input, classifies it using the trained model, and selects a response from the appropriate intent.
- **Display**: The chat interface updates in real-time to show the conversation between the user and the chatbot. The user can continue interacting with the bot until they decide to end the conversation.

## 🤝 Contributing

We welcome contributions! If you have suggestions or improvements, please follow these steps:

1. **Fork the repository**
2. **Create a new branch**
3. **Make your changes**
4. **Submit a pull request**

Happy coding! 😊
import streamlit as st
import requests

st.title("AI Generated Quiz")

# Input for quiz topic
quiz_topic = st.text_input('Quiz topic input', 'Animals in nature')
st.write('Current quiz topic is', quiz_topic)

# Input for number of questions
number_of_questions = st.number_input('Number of questions', min_value=0, value=5)
st.write('Current number of questions is', number_of_questions)

# Function to generate quiz
def generate_quiz(quiz_topic, number_of_questions):
    # Prepare the data for the POST request
    json = {
        'quiz_topic': quiz_topic,
        'number_of_questions': number_of_questions
    }
    
    # Send the request to the Flask server
    try:
        response = requests.post('http://127.0.0.1:8080/generate_quiz', json=json)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: Server responded with status code {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

# Button to generate quiz
if st.button('Generate Quiz'):
    st.write('Generating quiz...')
    quiz = generate_quiz(quiz_topic, number_of_questions)
    if isinstance(quiz, dict):
        st.write(quiz.get('quiz', 'No quiz generated.'))
    else:
        st.write(quiz)

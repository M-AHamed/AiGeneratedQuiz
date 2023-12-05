import streamlit as st
import requests

st.title("AI Generated Quiz")
# Input for quiz topic
quiz_topic = st.text_input('Quiz topic input', 'Animals in nature')
st.write('Current quiz topic is', quiz_topic)

# Input for number of questions
number_of_questions = st.number_input('Number of questions', min_value=1, value=5)
st.write('Current number of questions is', number_of_questions)

# Function to generate quiz
def generate_quiz(quiz_topic, number_of_questions):
    json_data = {
        'quiz_topic': quiz_topic,
        'number_of_questions': number_of_questions
    }
    try:
        response = requests.post('http://127.0.0.1:8080/generate_quiz', json=json_data)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: Server responded with status code {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"
# Initialize session state
if 'quiz_data' not in st.session_state:
    st.session_state.quiz_data = None
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}
# Generate quiz button
if st.button('Generate Quiz'):
    quiz_response = generate_quiz(quiz_topic, number_of_questions)
    if isinstance(quiz_response, dict) and 'questions' in quiz_response:
        st.session_state.quiz_data = quiz_response
        st.session_state.user_answers = {}

if st.session_state.quiz_data:
    if 'questions' in st.session_state.quiz_data:
        for idx, question in enumerate(st.session_state.quiz_data['questions'], start=1):
            choices = question['choices']
            answer_choices = [f"{key}: {value}" for key, value in choices.items()]
            st.session_state.user_answers[idx] = st.radio(f"Q{idx}: {question['question']}", answer_choices, key=str(idx))
        # Submit answers button
        if st.button('Submit Answers'):
            for idx, question in enumerate(st.session_state.quiz_data['questions'], start=1):
                selected_answer = st.session_state.user_answers[idx].split(':')[0]  # Extract choice letter
                correct_answer_key = next(key for key, value in question['answer'].items() if value)
                if selected_answer == correct_answer_key:
                    st.success(f"Q{idx}: Correct! Your answer: {selected_answer}")
                else:
                    correct_answer = question['choices'][correct_answer_key]
                    st.error(f"Q{idx}: Incorrect! Your answer: {selected_answer} - Correct answer: {correct_answer_key}: {correct_answer}")


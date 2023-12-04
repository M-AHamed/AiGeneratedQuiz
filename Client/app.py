import streamlit as st

st.title("AI Generated Quiz")


# input quiz topic
# input number of questions

# input quiz topic
# quiz topic, default is 'Animals in nature'
quiz_topic = st.text_input('Quiz topic input', 'Animals in nature')
st.write('Current quiz topic is', quiz_topic)
# input number of questions
# number of questions, default is 0
number_of_questions = st.number_input('Number of questions', 0)
st.write('Current number of questions is', number_of_questions)

# button to generate quiz
if st.button('Generate Quiz'):
    st.write('generating quiz...')
    st.write('Quiz topic is:', quiz_topic,' || Number of questions is:', number_of_questions)
    # call the generate quiz function
    # generate_quiz(quiz_topic, number_of_questions)

# generate the quiz function
def generate_quiz(quiz_topic, number_of_questions):
    # pass the quiz topic and number of questions to the server via route
    json = {
        'quiz_topic': quiz_topic,
        'number_of_questions': number_of_questions
    }
    # send the json to the server
    # server route is /generate_quiz
    response = requests.post('http://localhost:5000/generate_quiz', json=json)
    pass


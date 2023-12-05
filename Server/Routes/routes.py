from flask import Blueprint, request, jsonify
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=OPENAI_API_KEY)

quiz_routes = Blueprint('quiz_routes', __name__)

# Function to interact with OpenAI API using the chat format
def create_quiz(topic, num_questions):
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a quiz creator given a topic and a number of questions you will return a quiz. Multiple choice with 4 choices for each question, and one correct answer marked with a true."},
                {"role": "user", "content": f"Topic: {topic}, number of questions: {num_questions}"}
            ]
        )
        # Extract the text content from the completion object
        quiz_text = completion.choices[0].message  # Ensure this is a string
        print(quiz_text)
        print("Quiz generated successfully ----------------------------------------")
        return quiz_text  # Remove any leading/trailing whitespace
    except Exception as e:
        return str(e)  # Convert exception to string to ensure JSON serializability

@quiz_routes.route('/generate_quiz', methods=['POST'])
def generate_quiz_route():
    json_data = request.get_json()
    
    quiz_topic = json_data.get('quiz_topic')
    number_of_questions = json_data.get('number_of_questions')

    if not quiz_topic or not isinstance(quiz_topic, str):
        return jsonify({'error': 'Quiz topic is required and must be a string'}), 400

    if not number_of_questions or not isinstance(number_of_questions, int):
        return jsonify({'error': 'Number of questions is required and must be an integer'}), 400

    quiz = create_quiz(quiz_topic, number_of_questions)

    if isinstance(quiz, str):
        return jsonify({'quiz': quiz})
    else:
        return jsonify({'error': quiz}), 500  # 'quiz' should be a string, either the quiz or an error message

# Quiz generation GET route for testing
@quiz_routes.route('/generate_quiz_get', methods=['GET'])
def generate_quiz_get_route():
    return "Quiz Generation GET route"

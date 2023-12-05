from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI client with the API key
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Create a chat completion
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a quiz creator given a topic and a number of questions you will return a quiz. multiple choice with 4 choices for each question, and one correct answer marked with a true"},
    {"role": "user", "content": "Topic: Animals in nature, number of questions: 5"}
  ]
)

# Print the response
print(completion.choices[0].message)

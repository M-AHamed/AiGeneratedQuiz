from flask import Flask
from Routes.routes import quiz_routes

app = Flask(__name__)

# Register the blueprint from routes.py
app.register_blueprint(quiz_routes)

if __name__ == '__main__':
    app.run(debug=True, port=8080)

from flask import Flask
from flask_restx import Api
from api.student import api as students
from db.db import init_db
from flask_cors import CORS

app = Flask(__name__)

CORS(
    app,
    resources={
        r"/*": {
            "origins": ["http://127.0.0.1:8000"],  # Get origin from env with fallback
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"],
            "supports_credentials": True,
        }
    },
)

password = "12345"

init_db(app)

# Initialize Flask-RESTx API and register the students namespace
api = Api(app)
api.add_namespace(students)  # Add the students namespace to the API

if __name__ == "__main__":
    app.run(debug=True, port=6969, host="0.0.0.0")

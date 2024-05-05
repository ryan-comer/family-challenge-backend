from flask import Flask, request, jsonify
from flask_cors import CORS

from dotenv import load_dotenv
load_dotenv()

from routes.challenges import challenges

app = Flask(__name__)
CORS(app)

# Import the routes
app.register_blueprint(challenges)

if __name__ == '__main__':
    app.run()
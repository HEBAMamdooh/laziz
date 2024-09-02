import os
from dotenv import load_dotenv
from flask import Flask, render_template

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Access the environment variables
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")


if __name__ == '__main__':
	app.run(debug=True)

from flask import Flask, request, render_template, session
from sentiment_model import analyze_sentiment
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
app.secret_key = os.getenv("SECRET_KEY")

# Initialize history list
history = []

@app.route('/', methods=['GET', 'POST'])
def index():
    # Initialize sentiment for GET requests
    sentiment = None

    # Process user input and run the sentiment model
    if request.method == 'POST':
        text = request.form["user_input"]
        sentiment = analyze_sentiment(text)
        history.append((text, sentiment)) 
        history[:] = history[-10:]
        
    return render_template('index.html', sentiment=sentiment, history=history)

if __name__ == '__main__':
    app.run(debug=True)

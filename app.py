from flask import Flask, render_template, Response
from utils.speech_engine import start_recognition

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def generate_text():
    for text in start_recognition():
        yield f"data: {text}\n\n"

@app.route('/stream')
def stream():
    return Response(generate_text(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)

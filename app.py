from flask import Flask, request, jsonify,render_template
from AI_Chatbot import chat_bot

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

@app.post("/predict")
def predict():
    user_input = request.get_json.get['user_input']
    bot_response = chat_bot(user_input) 
    message = {"answer":bot_response}
    return jsonify({'response': message})

if __name__ == '__main__':
    app.run(debug=True)

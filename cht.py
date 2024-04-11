from flask import Flask, render_template, request, jsonify
from AI_Chatbot import chat_bot

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['user_input']
    bot_response = chat_bot(user_input)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)

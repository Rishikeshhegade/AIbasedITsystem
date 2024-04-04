from flask import Flask, request, jsonify
from AI_Chatbot import chat_bot

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    # Receive message from the website
    user_message = request.json['message']
    
    # Process the message and generate a response (replace this with your chatbot logic)
    bot_response = "You said: " + user_message
    
    # Return the response to the website
    return jsonify({'response': bot_response})
    
if __name__ == '__main__':
    app.run(debug=True)

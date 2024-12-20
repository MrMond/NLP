from flask import Flask, jsonify, request

from ollama import ChatResponse
from ollama import chat


system_message = ""
context_message = ""

app = Flask(__name__)


@app.route('/generate_recommendations', methods=['POST'])
def generate_recommendations():

    messages = []
    messages.append({'role': 'system', 'content': system_message})
    messages.append({'role': 'system', 'content': context_message})
    
    body = request.get_json()
    conversation_history = body.get('conversation_history', [])
    
    for message in conversation_history:
        messages.append({'role': message['role'],'content': message['content']})
    
    response: ChatResponse = chat(model='llama3.2', messages=messages)

    messages.append({'role': 'assistant', 'content': response['message']['content']})

    messages = messages[2:]
    
    print(messages)

    return jsonify({
        'conversation_history': messages,
    })


if __name__ == '__main__':
    app.run(port=5000)

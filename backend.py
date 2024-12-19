from flask import Flask, jsonify, request
from utility.Chat import Chat

system_message = ""
context_message = ""

app = Flask(__name__)


@app.route('/generate_recommendations', methods=['POST'])
def generate_recommendations():

    chat = Chat()
    chat.add_message('system', system_message)
    chat.add_message('system', context_message)

    body = request.get_json()
    user_message = body["message"]
    conversation_history = body.get('conversation_history', [])

    for message in conversation_history:
        chat.add_message(message['role'], message['content'])

    chat.add_message('user', user_message)
    chat.generate_response()

    chat.conversation_history = chat.conversation_history[2:]

    return jsonify({
        'conversation_history': chat.conversation_history
    })


if __name__ == '__main__':
    app.run(port=5000)

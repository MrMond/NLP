from flask import Flask, jsonify, request

from ollama import ChatResponse
from ollama import chat
from utility.EntityExtractor import EntityExtractor
from utility.variables import system_message
from utility.nba_data import fetch_context

app = Flask(__name__)


@app.route('/generate_recommendations', methods=['POST'])
def generate_recommendations():

    messages = []
    messages.append({'role': 'system', 'content': system_message})
    messages.append({'role': 'system', 'content': "Introduce yourself"})
    
    body = request.get_json()
    conversation_history = body.get('conversation_history', [])
    
   
        
    # get the last message content
    last_message = conversation_history[-1]['content']
    
    extractor = EntityExtractor()
    entities = extractor.extract_entities(last_message)
    
    context = fetch_context(entities)
    context = str(context)
    messages.append({'role': 'system', 'content': context})
    
    for message in conversation_history:
        messages.append({'role': message['role'],'content': message['content']})
    
    print(f"Messages: {messages}")
    try:
        response: ChatResponse = chat(model='llama3.2', messages=messages)
        print(response)
    except Exception as e:
        print(f"Error: {e}")

    messages.append({'role': 'assistant', 'content': response['message']['content']})
    

    return jsonify({
        'conversation_history': messages,
    })


if __name__ == '__main__':
    app.run(port=5000)

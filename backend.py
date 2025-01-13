from flask import Flask, jsonify, request

from ollama import ChatResponse
from ollama import chat
from utility.EntityExtractor import EntityExtractor
from utility.variables import system_message
from utility.nba_data import fetch_context
from utility.web_scraper import receive_vector_store

app = Flask(__name__)

vector_db = receive_vector_store()

@app.route('/generate_recommendations', methods=['POST'])
def generate_recommendations():

    messages = []
    messages.append({'role': 'system', 'content': system_message})
    
    body = request.get_json()
    conversation_history = body.get('conversation_history', [])
    
   
        
    # get the last message content
    last_message = conversation_history[-1]['content']
    
    # extract entities from the last message
    extractor = EntityExtractor()
    entities = extractor.extract_entities(last_message)
    
    # fetch context from the API
    api_context = fetch_context(entities)
    api_context = str(api_context)
    messages.append({'role': 'system', 'content': api_context})
    
    # fetch context from the vector database
    db_context = vector_db.similarity_search(last_message)
    # Extract and format document content
    formatted_context = "\n\n".join(
        f"Source: {doc.metadata.get('source', 'Unknown')}\nContent: {doc.page_content}"
        for doc in db_context
    )
    
    print(entities)
    print("\n")
    print(formatted_context)
    print("\n")
    
    messages.append({'role': 'system', 'content': formatted_context})
    
    for message in conversation_history:
        messages.append({'role': message['role'],'content': message['content']})
    
    try:
        response: ChatResponse = chat(model='llama3.2', messages=messages)
    except Exception as e:
        print(f"Error: {e}")

    messages.append({'role': 'assistant', 'content': response['message']['content']})
    

    return jsonify({
        'conversation_history': messages,
    })


if __name__ == '__main__':
    app.run(port=5000)

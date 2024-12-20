import requests
import streamlit as st

if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []
    
if 'user_input' not in st.session_state:
    st.session_state.user_input = ""

if 'send_clicked' not in st.session_state:
    st.session_state.send_clicked = False  # To track send button click

def clear_input():
    st.session_state.user_input = st.session_state.input_field
    st.session_state.input_field = ""

def get_recommendations():
    try:
        response = requests.post(
            url='http://localhost:5000/generate_recommendations',
            headers={'Content-Type': 'application/json'},
            json={
                'conversation_history': st.session_state.conversation_history,
            }
        )
        response.raise_for_status()
        response_data = response.json()

        st.session_state.conversation_history = response_data.get(
            'conversation_history', [])
        return None

    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return None

st.title("Fantasy Recommender")

chat_container = st.container()

with chat_container:
    for msg in st.session_state.conversation_history:
        if msg['role'] == 'user':
            st.chat_message('user').markdown(msg['content'])
        elif msg['role'] == 'assistant':
            st.chat_message('assistant').markdown(msg['content'])
            
    # Display the current user input immediately after appending
    if st.session_state.send_clicked and st.session_state.user_input:
        st.chat_message('user').markdown(st.session_state.user_input)

with st.container():
    col1, col2 = st.columns([0.87, 0.12])

    with col1:
        user_input = st.text_input(
            "", 
            placeholder="Type your message here:",
            label_visibility="collapsed",
            key="input_field",
            on_change=clear_input
        )

    with col2:
        send_button = st.button("Send", on_click=lambda: st.session_state.update(send_clicked=True))
    
    # Handle input logic after send_button is clicked
    if st.session_state.send_clicked and st.session_state.user_input:
        st.session_state.conversation_history.append({
            'role': 'user',
            'content': st.session_state.user_input,
        })

        st.session_state.send_clicked = False  # Reset send button state
        get_recommendations()
        st.rerun()
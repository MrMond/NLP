import requests
import streamlit as st


if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []


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
        elif msg['role'] == 'bot':
            st.chat_message('bot').markdown(msg['content'])


with st.container():

    col1, col2 = st.columns([0.87, 0.12])

    with col1:
        user_input = st.text_input("", placeholder="Type your message here:",
                                   label_visibility="collapsed")

    with col2:
        send_button = st.button("Send")

    if send_button and user_input:
        st.session_state.conversation_history.append({
            'role': 'user',
            'content': user_input,
        })

        get_recommendations()
        st.rerun()

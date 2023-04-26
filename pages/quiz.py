import streamlit as st
from streamlit_chat import message
import json
from typing import List
from pathlib import Path




questions = []
uploaded_file = st.file_uploader("Upload JSON file", type=["json"])

if uploaded_file is not None:
    data = json.load(uploaded_file)

    
    for d in data:
        if 'question' in d:
            questions.append(d['question'])
        if 'Question' in d:
            questions.append(d['Question'])



if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

if 'current_question' not in st.session_state:
    st.session_state['current_question'] = 0



if st.session_state['current_question'] <= len(questions):
    current_question = questions[st.session_state['current_question']]
    message(current_question['question'], is_user=False, key=str(
        st.session_state['current_question']))

    with st.form(key="input_form"):
        user_input = st.text_input("You: ", "", key="input")
        submit_button = st.form_submit_button(label="Submit")

    if submit_button and user_input:
        st.session_state['past'].append(user_input)
        st.session_state['current_question'] += 1
        st.experimental_rerun()

    st.sidebar.header("Conversation History")
    for i, question in enumerate(questions):
        if i < st.session_state['current_question']:
            st.sidebar.write("Bot: "+question['question'])
            st.sidebar.write(
                "You: " + st.session_state['past'][i])

else:
    responses = []
    for i, question in enumerate(questions):
        response = {
            "question": question['question'],
            "answer": st.session_state['past'][i]
        }
        responses.append(response)

    user.assignments[st.session_state['pos']] = {
        "topic": st.session_state['selected_topic'], "responses": responses}
    save_users(users)

    message("Thank you for answering all the questions. Your responses have been saved.",
            is_user=False, key=str(st.session_state['selected_topic']))
    st.sidebar.write(
        "Thank you for answering all the questions. Your responses have been saved.")
    st.session_state['current_question'] = 0
    st.session_state['selected_topic'] = ""
    st.session_state['pos'] = None
    st.session_state['past'] = []
    st.session_state['generated'] = []

    # st.stop()
    st.sidebar.download_button(
        label="Download Responses",
        data=json.dumps(responses),
        file_name="responses.json",
        mime="application/json"
    )

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])+1, 1, 1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i],
            is_user=True, key=str(i) + '_user')
        st.sidebar.write("Bot: ", st.session_state["generated"][i])

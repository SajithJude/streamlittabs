import streamlit as st
import json

# Use Streamlit's file uploader to upload the first JSON file
uploaded_file_1 = st.file_uploader("Upload first JSON file", type=["json"])

# Use Streamlit's file uploader to upload the second JSON file
uploaded_file_2 = st.file_uploader("Upload second JSON file", type=["json"])

# If both files have been uploaded, extract the answers from both files
if uploaded_file_1 is not None and uploaded_file_2 is not None:
    data_1 = json.load(uploaded_file_1)
    data_2 = json.load(uploaded_file_2)

    # Extract the answers from the first file
    student_answer = []
    actual_answer = []
    for d in data_1:
        if 'answer' in d:
            actual_answer.append(d['answer'])
        if 'Answer' in d:
            actual_answer.append(d['Answer'])
        if 'student_answer' in d:
            student_answer.append(d['student_answer'])
        if 'Student_Answer' in d:
            student_answer.append(d['Student_Answer'])

    # Extract the answers from the second file
    for d in data_2:
        if 'answer' in d:
            actual_answer.append(d['answer'])
        if 'Answer' in d:
            actual_answer.append(d['Answer'])
        if 'student_answer' in d:
            student_answer.append(d['student_answer'])
        if 'Student_Answer'

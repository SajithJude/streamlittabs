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
    for d in data_1:
        if 'answers' in d:
            student_answer.append(d['answers'])

    # Extract the answers from the second file
    actual_answer = []
    for d in data_2:
        if 'answers' in d:
            actual_answer.append(d['answers'])

    # Do something with the student_answer and actual_answer variables
    st.write("Student answer:", student_answer)
    st.write("Actual answer:", actual_answer)

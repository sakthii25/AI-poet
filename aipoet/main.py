import openai
import os
import streamlit as st
openai.api_key = os.getenv("openaiapikey")
def getresponse(msg):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Write a poem on " + msg + " with 8 to 12 lines where each line contains 4 to 5 words"}]
    )
    reply = response.choices[0].message.content
    return reply
msg = st.text_input("Enter a topic: ")
if msg:
    st.write(getresponse(msg))

import openai
import os
import streamlit as st
openai.api_key = os.getenv("openaiapikey")
def getresponse(msg):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Write a poem on this topic " + msg + " the poem will look like a shakesphere's poem"}]
    )
    reply = response.choices[0].message.content
    return reply
msg = st.text_input("Enter Poem Title: ")
if msg:
    st.write("Here is your Poem:" + "\n" + getresponse(msg))

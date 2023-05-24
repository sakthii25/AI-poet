import openai
import os
import streamlit as st
openai.api_key = os.getenv("openaiapikey")
def getresponse(msg):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "based on topic wrtie a creative poem in a poem format"
                                              "the topic is " + msg + " first you have to give heading "
                                                                      "to the poem and write the poem in a crisp manner"}]
    )
    reply = response.choices[0].message.content
    return reply
msg = st.text_input("Enter a topic: ")
if msg:
    st.write(getresponse(msg))
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# COnfigure the API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#  Function to Load Google Gemini Model and provide qurey as a response

def get_gemini_response(question,prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt[0],question])
    return response.text

#  Funtion to retrive qurey from the sql database

def read_sql_qurey(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt = [
    """
    You are an expert in converting English question to SQL qurey!
    The SQL database has the name PLAYER and Following Columns - NAME, AGE, GOALS \n\nFor example,\nExample 1 - How many players are present in PLAYER?, The SQl command will be SELECT COUNT(*) FROM PLAYER;\nExample 2 - Tell player who has more than 800 goals?, The SQL command will be something like this SELECT * FROM PLAYER where  GOALS > 800;
    also the sql code should not have ``` in beginning or end and sql word in the output.

"""
]

st.set_page_config(page_title="I can Retrive Any SQL qurey")
st.header("Gemini App to Retrive SQL Data")
question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

#  If submit is click
if submit:
    response = get_gemini_response(question,prompt)
    print(response)
    data = read_sql_qurey(response,"player.db")
    st.subheader("The Response is ")
    for row in data:
        print(row)
        st.header(row)

import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images\photo.png",width=500)

with col2:
    st.title("Suhas M")
    content = """I am a proactive individual from Bangalore, India, with a strong academic foundation and a passion for leadership. Currently pursuing a B.Tech in Electronics and Communication at SRM Institute of Science and Technology, I excel in effective communication, team management, and financial analysis—skills that are vital in today’s professional landscape.

Beyond academics, I channel my creativity through music as a guitar enthusiast and stay active by playing volleyball. These diverse interests enhance my adaptability, resilience, and ability to thrive in both team-oriented and independent environments."""
    st.info(content)

col3, col4 = st.columns(2)


df = pandas.read_csv("data.csv",sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


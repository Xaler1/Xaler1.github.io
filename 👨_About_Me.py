import streamlit as st

st.set_page_config(page_title="👨 About Me", page_icon=":man:", layout="wide")

st.title("Alexander Radchenko")

description = """
Welcome to my personal website! I am a Data Scientist and Machine Learning Engineer. 
I am passionate about solving complex problems and building intelligent systems. 
I have experience in building and deploying machine learning models, data analysis, and software development.
"""
description = description.replace("\n", " ")

st.subheader(description)

import streamlit as st
import base64

st.set_page_config(page_title="📄 CV", page_icon=":page_facing_up:")

st.title("My CV")

with open("./Alexander Radchenko CV.pdf", "rb") as f:
    pdf = f.read()
base64_pdf = base64.b64encode(pdf).decode('utf-8')
pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="1000" type="application/x-google-chrome-pdf">'
st.markdown(pdf_display, unsafe_allow_html=True)
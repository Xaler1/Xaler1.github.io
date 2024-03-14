import streamlit as st
from streamlit_js_eval import streamlit_js_eval
import base64

st.set_page_config(page_title="📄 CV", page_icon=":page_facing_up:")

st.title("My CV")

with open("./Alexander Radchenko CV.pdf", "rb") as f:
    pdf = f.read()
base64_pdf = base64.b64encode(pdf).decode('utf-8')
pdf_display =  f"""<embed
class="pdfobject"
type="application/pdf"
title="Embedded PDF"
src="data:application/pdf;base64,{base64_pdf}"
style="overflow: auto; width: 100%; height: 100%;">"""

# Displaying File
st.markdown(pdf_display, unsafe_allow_html=True)
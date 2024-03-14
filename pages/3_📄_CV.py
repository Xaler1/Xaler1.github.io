import streamlit as st
from streamlit_js_eval import streamlit_js_eval
import base64

st.set_page_config(page_title="📄 CV", page_icon=":page_facing_up:")

st.title("My CV")

js_code = """
const iframes = document.getElementsByTagName('iframe');
for (let i = 0; i < iframes.length; i++) {
    iframes[i].removeAttribute('sandbox');
}
"""
streamlit_js_eval(js_expressions=js_code, key='removeSandbox')

with open("./Alexander Radchenko CV.pdf", "rb") as f:
    pdf = f.read()
base64_pdf = base64.b64encode(pdf).decode('utf-8')
pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="1000" type="application/pdf">'
#st.markdown(pdf_display, unsafe_allow_html=True)
alt_pdf = f'<embed src="Alexander Radchenko CV.pdf" type="application/pdf" width="100%" height="100%" />'
st.markdown(pdf_display, unsafe_allow_html=True)


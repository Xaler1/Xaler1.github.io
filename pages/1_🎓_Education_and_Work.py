import streamlit as st
from pages.sections import education, work

st.set_page_config(page_title="🎓 Education and Work", page_icon=":graduation_cap:")

st.title("🎓 Education and Work Experience")

ed_tab, work_tab = st.tabs(["Education", "Work Experience"])

with ed_tab:
    education.run()

with work_tab:
    work.run()




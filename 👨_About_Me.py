import streamlit as st
from streamlit_js_eval import streamlit_js_eval

st.set_page_config(page_title="👨 About Me", page_icon=":man:", layout="wide")

st.title("Alexander Radchenko")
st.markdown("### First Year Robotics Masters Student at the GRASP Lab, University of Pennsylvania")

description = """
## Welcome to my personal website!

Welcome to my personal website! I’m Alexander Radchenko, a passionate advocate for automation and efficiency. 
I believe in the power of disassembling complex systems to uncover their core functionalities and reassembling them in a way that enhances performance and productivity. 
My journey in robotics and machine learning is driven by this philosophy, as I strive to create intelligent solutions that simplify life and work.

As a current Masters student in Robotics at the University of Pennsylvania, 
I specialize in Computer Vision and Reinforcement Learning, applying these cutting-edge technologies to the field of robotics. 
My academic excellence is reflected in my 3.9 GPA, and my hands-on experience includes a dissertation that achieved state-of-the-art results in language reasoning with visual cues.

My technical skills are diverse, encompassing programming languages like Python, Java, C, and C++, 
as well as expertise in data science and machine learning tools such as PyTorch, Pandas, and HuggingFace. 
I’ve also demonstrated my abilities in game and web development, with projects like the Graviton Android game and Unreal Engine plugins that have garnered significant attention.

I invite you to explore my site:
"""

description_2 = """
### Contact me!
- [alex.and.radchenko@gmail.com](mailto:alex.and.radchenko@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/xaler/)
"""

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(description)
    if st.button("‎ " * 32 + "View my CV" + "‎ " * 32, type="primary"):
        st.switch_page("pages/3_📄_CV.py")
    if st.button("See my educational and work experiences", type="primary"):
        st.switch_page("pages/1_🎓_Education_and_Work.py")
    if st.button("‎ " * 13 + "Learn more about my projects" + "‎ " * 13, type="primary"):
        st.switch_page("pages/2_💻_Projects.py")
    st.markdown("Or look at the snapshot below!")

    st.markdown(description_2)

with col2:
    st.image("./profile_pic.jpg", caption="Me!", use_column_width=True)

js_code = """var anchors = document.getElementsByTagName('a');
for (var i = 0; i < anchors.length; i++) {
    anchors[i].setAttribute('target', '_self');
}"""


streamlit_js_eval(js_expressions=js_code, key='setTargetSelf')

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

vln_description = """## Language Navigation with Visual Cues
This was my final year project at the University of St Andrews. Which ended up being presented at [ICRA 2023 in London](https://sites.google.com/view/cognitive-modeling-icra2023-ws/contributions?authuser=0#h.9dehx8dlga4n).
The goal was to create an end-to-end high level task planning and execution system for a robotic system. By combining GPT-3 and an open-vocabulary object detection model I was able 
to create a system that could understand natural language instructions, and execute them in a simulated environment based on observations from that environment.

Using Python, Lua, PyTorch, GPT-3 and various Open vocabulary object detection models.
"""

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(description)
    st.download_button("‎ " * 27 + "Download my CV" + "‎ " * 27, type="primary", file_name="Alexander_Radchenko_CV.pdf", data="Alexander_Radchenko_CV.pdf")
    if st.button("See my educational and work experiences", type="primary"):
        st.switch_page("pages/1_🎓_Education_and_Work.py")
    if st.button("‎ " * 13 + "Learn more about my projects" + "‎ " * 13, type="primary"):
        st.switch_page("pages/2_💻_Projects.py")
    st.markdown("Or look at the snapshot below!")

    st.markdown("### Some cool projects I've worked on:")
    with st.container(border=True):
        container_col1, container_col2 = st.columns([1, 3])
        with container_col1:
            st.markdown("")
            st.image("./language_navigation.png")
        with container_col2:
            st.markdown(vln_description)

    st.markdown(description_2)



with col2:
    st.image("./profile_pic.jpg", caption="Me!", use_column_width=True)

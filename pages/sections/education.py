import streamlit as st

def run():
    st.subheader("My education background in reverse chronological order:")

    st.markdown("### September 2021 - May 2023")
    col1, col2 = st.columns([2, 1], gap="small")
    with col1:
        st.markdown("## University of Pennsylvania")

    with col2:
        st.image("./upenn_logo.png", width=200)

    description = """
        >First year Robotics Masters student at the [GRASP Lab](https://www.grasp.upenn.edu/).
        >Studying deep learning, computer vision, and robotics.
        >
        >Overall GPA: 3.9
        
        >Semester 2:
        >- CIS6200: Advanced Topics in Deep Learning
        >
        >   Covering all the latest and cutting-edge papers in a wide variety of deep learning topics
        >
        >   Coursework project: Text Guided Image Colorization using diffusion models
        >- ESE6500: Learning in Robotics
        >
        >   Kalman filters, SLAM, NeRFs, control planning, and reinforcement learning
        >
        >- MEAM5200: Intro to Robotics
        >
        >   Working with the Franka Panda robot using ROS to implement motion planning algorithms
    
        >Semester 1 (GPA 3.9):
        >- CIS5810: Computer Vision
        >
        >   Analytical and machine learning approaches to computer vision. [Github](https://github.com/Xaler1/WhatsForDinner)
        >
        >   Coursework project: Automatic ingredient recognition in fridge pictures and recipe generation
        >- ESE5140: Graph Neural Networks
        >
        >   Used GNNs for node processing and group agent coordination
        >- ESE5460: Principles of Deep Learning
        >
        >   All the mathematical foundations for deep learning, from linear regression to Transformers
        >
        >   Coursework project: Heart disease prediction using ECG data using Transformers. [Github](https://github.com/Xaler1/DLProject)
        """
    st.markdown(description)

    st.divider()

    st.markdown("### September 2020 - May 2023")
    col1, col2 = st.columns([2, 1], gap="small")
    with col1:
        st.markdown("## University of St Andrews")

    with col2:
        st.image("./sta_logo.png", width=250)

    description = """
        >Bachelor of Science in Computer Science with Honours. 
        >Admitted directly into the second year of the program. 
        >Graduated in May of 2023.
        >
        >Overall GPA: 4.0
        
        >Year 4:
        >- Research Project on "Language Reasoning with Visual Ques"
        >- Machine Learning
        >- NLP
        >- Signal Processing
        
        >Year 3:
        >- Group software project using Java, SQL, and JavaScript: A federated network of journals for peer-reviewing code. 
        >- Databases
        >- Algorithms
        
        >Year 2:
        >- Object-Oriented Programming
        >- Linear Algebra
        >- Probability and Statistics
        >- Vector Calculus 
        """
    st.markdown(description)
import streamlit as st

def run():
    st.subheader("My work experience in reverse chronological order:")

    st.markdown("### June 2023 - August 2023")
    col1, col2 = st.columns([2, 1], gap="small")
    with col1:
        st.markdown("## Siguler Guff\n\n### Investment Analyst Intern")
    with col2:
        st.image("./siguler-guff_logo.png", width=200)

    description = """
    >Private equity firm with $18B in assets under management. [Official Website](https://www.sigulerguff.com/)
    >
    >- Conduct market mapping and analysis on potential investors in the European market
    >- Analyzed company profiles
    >- Built a chatbot for interactive analysis of Preqin data
    """
    st.markdown(description)

    st.divider()

    st.markdown("### July 2022 - September 2022")
    col1, col2 = st.columns([2, 1], gap="small")
    with col1:
        st.markdown("## Featurespace\n\n### Data Science Intern")
    with col2:
        st.image("./featurespace_logo.png", width=200)

    description = """
    >Leading provider of Enterprise Financial Crime Prevention software. [Official Website](https://www.featurespace.com/)
    >
    >- Used Python, Pandas and the Great Expectations library to create an automated data health check pipeline. Using statistical analysis, data profiling and empirical rule validation to ensure data quality.
    >  Generating reports and visualization in a dashboard to be used by the data science team.
    >- Developed a tool for ML model robustness testing. Using simulated data poisoning and/or outages to test the effects on the model's performance.
    >- Using the tool for robustness testing evaluated the model to identify weakness and what factors influence the model's predictions, uncovering some interesting correlations. 
    """
    st.markdown(description)

    st.divider()

    st.markdown("### June 2021 - August 2021")
    col1, col2 = st.columns([2, 1], gap="small")
    with col1:
        st.markdown("## Agroxy\n\n### Machine Learning Intern")
    with col2:
        st.image("./agroxy_logo.png", width=200)

    description = """
    >Ukranian startup developing a digital platform for trading agricultural commodities. [Official Website](https://agroxy.com/)
    >
    >- Used Python, TensorFlow, OpenCV and various map APIs to develop a machine learning model to identify and size grain silos from satellite images
    >- Created a database of silos locations across most of Europe
    """
    st.markdown(description)

    st.divider()

    st.markdown("### July 2019 - August 2019")

    col1, col2 = st.columns([2, 1], gap="small")
    with col1:
        st.markdown("## DataSpace\n\n### Software Development Intern")
    with col2:
        st.image("./dataspace_logo.png", width=200)

    description = """
    >Datacenter and cloud services provider. [Official Website](https://www.dataspace.ru/en/)
    >
    >- Used Python to develop a data processing algorithm to automate sever usage data by clients, sorting and creating billing reports
    >- Automated support ticket creation from client emails
    """
    st.markdown(description)


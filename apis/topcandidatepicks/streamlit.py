import streamlit as st
from main import get_applicants
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Applicant Finder", page_icon=":mag:", layout="wide")

# Apply custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #000000;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Candidates Top Pick")

job_id = st.text_input("Enter Job ID:")
num_candidates = st.number_input("Enter Number of Candidates:", min_value=1, max_value=100, value=5)

if st.button("Get Applicants"):
    if job_id:
        result = get_applicants(job_id, num_candidates)
        if result != "Error":
            st.write(f"Top {num_candidates} candidates for Job ID {job_id}:")
            if result:
                # Convert the result to a DataFrame
                df = pd.DataFrame(result)
                # Select relevant columns
                df = df[['user_id', 'name', 'email', 'Score']]
                # Display the DataFrame as a table
                st.table(df)
            else:
                st.write("No candidates found.")
        else:
            st.error("Error fetching data. Please try again later.")
    else:
        st.warning("Please enter a Job ID.")


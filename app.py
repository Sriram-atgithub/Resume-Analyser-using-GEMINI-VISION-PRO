# Import the necessary libraries
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
import base64
import io
import time
from streamlit import session_state as state

# Load environment variables
load_dotenv()

# Configure GenerativeAI (assuming API key is set in environment variables)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get Gemini response (assuming text extraction from PDF)
def get_gemini_response(input_text, pdf_text, prompt):
  try:
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_text, pdf_text, prompt])
    return response.text
  except Exception as e:
    st.error(f"An error occurred: {e}")
    return None

# Streamlit UI setup
st.set_page_config(page_title="ATS Resume Expert")

st.sidebar.markdown("## Resume Analyser - Gemini Vision Pro ")

st.sidebar.button("Menu Bar")

# Main page (About the App)
def about_app():
  st.header("Resume Analyser using GEMINI VISION PRO LLM")
  st.subheader("Home Page ")
  st.sidebar.markdown("Navigate through the other pages to know more the app, documentation and developer ")

  input_text = st.text_area("Job Description :", key="input", height=50, help="Enter the job description to analyze.")
  uploaded_file = st.file_uploader("Upload your resume in PDF format ", type=["pdf"], help="Upload your resume in PDF format.")

  st.markdown(" > Use the functionalities to find out variour aspects of the resume.")

  if uploaded_file is not None:
    st.write("Resume Uploaded successfully!✅")

  if st.button("Resume analysis ", help="Help you to find out your strenghts and weeknesses for the Job"):
    state.submission_type = 1

  if st.button("The missing skills ", help="Help you to find out the missing skills required for the Job"):
    state.submission_type = 2

  if st.button("Profile match(%)", help="Help you to find out your profile match in % with job description for the Job"):
    state.submission_type = 3

  if "submission_type" in state:
    handle_submission(state.submission_type, input_text, uploaded_file)


def handle_submission(submission_type, input_text, uploaded_file):
  if uploaded_file is None:
    st.warning("Please upload the resume ")
    return

  # Access filename using `name` attribute
  pdf_filename = uploaded_file.name

  # Text extraction (consider error handling and alternative libraries if PyPDF2 unsupported)
  try:
    import PyPDF2
    with open(uploaded_file.name, "rb") as f:
      pdf_reader = PyPDF2.PdfReader(f)
      pdf_text = ""
      for page in pdf_reader.pages:
        pdf_text += page.extract_text()
except Exception as e:
    st.error(f"Failed to process the uploaded PDF: {e}")
    return

    input_prompts = {
        1: """
        You are a hiring manager with expertise in data science, full-stack web development, big data engineering, devops, or data analysis.
        Review the provided resume against the job description. Evaluate whether the candidate's profile aligns with the role.
        Provide your evaluation highlighting the candidate's strengths as "Your Strengths" and weaknesses as "Weaknesses" in relation to the specified job requirements.
        """,
        2: """
        Identify the missing keywords in the resume compared to the job description and list them as the missing skills.
        """,
        3: """
        You are an experienced ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality.
        Evaluate the resume against the provided job description. Provide the percentage match if the resume aligns with the job description.
        Present the output in the following format: 
        - **Candidate Name**: [Candidate Name]
        - **Profile Match**: [Job match by analysing job description and resume and give it in percentage]
        - **Skills you already have**: [matched keywords and with similar context keywords by finding it from job description and resume]
        - **The skills that you miss**: [missing keywords and with similar context keywords from job description and resume]
        - **Final thoughts**: [bullet points with candidate name and percentage match and with similar context keywords from job description and resume]
        """
    }

    response = get_gemini_response(input_text, pdf_content, input_prompts[submission_type])
    if response is not None:
        if submission_type == 1:
            st.subheader("My ATS Evaluation about your resume:")
            st.write(response)
        elif submission_type == 2:
            st.subheader("Skills Missing from Resume ❎:")
            st.write(response)
        elif submission_type == 3:
            st.subheader("Profile Match Report 📄")
            st.write(response)

# Documentation page
def about_the_app():
    st.subheader("Resume Analyser using GEMINI VISION PRO")
    st.write("### Information about the app")
    st.markdown(" - This app runs on google's gemini vision pro.") 
    st.markdown(" - It analyse the resume to give tailored insights on the job that a person wants to apply")
    st.image("Flowchart.png", caption="App Working Process")
    st.sidebar.markdown("Navigate through the other pages to know more the app, documentation and developer 🔎")

def documentation():
    st.subheader("Resume Analyser using GEMINI VISION PRO")
    st.write("### Documentation references: 📒")
    st.markdown("[Python Documentation](https://docs.python.org/3)")
    st.markdown("[Streamlit Documentation](https://docs.streamlit.io)")
    st.markdown("[Gemini API Documentation](https://ai.google.dev/tutorials/quickstart)")
    st.markdown("[Python dotenv Documentation](https://pypi.org/project/python-dotenv/)")
    st.markdown("[Pdf2image Documentation](https://pypi.org/project/pdf2image/)")
    st.sidebar.markdown("Navigate through the other pages to know more the app, documentation and developer 🔎")

# About the Author page
def about_developer():
    st.subheader("Resume Analyser using GEMINI VISION PRO")
    st.write("### About the developer")
    st.image("Photo.png", width=190)
    st.write("### Author: Sriram Ramakrishnan")
    st.write("I am a Data science and AI intern with expertise in machine learning and natural language processing.")
    st.write("Find more about me: 🔗")
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sriram-aiexpert/)")
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Sriram-atgithub)")
    st.sidebar.markdown("Navigate through the other pages to know more the app, documentation and developer 🔎")

# Run the app
if __name__ == "__main__":
    page = st.sidebar.radio("Sections", ["Home page 🏠", "About the app 💻", "Documentation 📒", "About the developer 👨‍💻"])
    if page == "Home page 🏠":
        about_app()
    elif page == "About the app 💻":
        about_the_app()
    elif page == "Documentation 📒":
        documentation()
    elif page == "About the developer 👨‍💻":
        about_developer()

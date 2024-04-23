  # Import the necessary libraries
from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import pdf2image
import google.generativeai as genai
import base64
import io
import time
from streamlit import session_state as state

# Load environment variables
load_dotenv()

# Configure GenerativeAI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get Gemini response
def get_gemini_response(input_text, pdf_content, prompt):
    try:
        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content([input_text, pdf_content[0], prompt])
        return response.text
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Function to set up input PDF
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        try:
            # Convert PDF to image
            images = pdf2image.convert_from_bytes(uploaded_file.read())
            first_page = images[0]

            # Convert to bytes
            img_byte_arr = io.BytesIO()
            first_page.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()

            pdf_parts = [
                {
                    "mime_type": "image/jpeg",
                    "data": base64.b64encode(img_byte_arr).decode()  # Encode to base64
                }
            ]
            return pdf_parts
        except Exception as e:
            st.error(f"An error occurred while processing the PDF: {e}")
            return None
    else:
        st.warning("Please upload a PDF file.")
        return None

# Streamlit UI setup
st.set_page_config(page_title="ATS Resume Expert")

st.sidebar.markdown("## Resume Analyser - Gemini Vision Pro 📄🔎")

st.sidebar.button("Menu Bar")


# Main page (About the App)
def about_app():
    st.header("Resume Analyser using GEMINI VISION PRO LLM")
    st.subheader("Home Page 🏠")
    st.sidebar.markdown("Navigate through the other pages to know more the app, documentation and developer 🔎")

    input_text = st.text_area("Job Description 📜:", key="input", height=50, help="Enter the job description to analyze.")
    uploaded_file = st.file_uploader("Upload your resume in PDF format 📑", type=["pdf"], help="Upload your resume in PDF format.")

    st.markdown(" > Use the functionalities to find out variour aspects of the resume.")

    if uploaded_file is not None:
        st.write("Resume Uploaded successfully!✅")

    if st.button("Resume analysis 📊", help="Help you to find out your strenghts and weeknesses for the Job"):
        state.submission_type = 1

    if st.button("The missing skills 📉", help="Help you to find out the missing skills required for the Job"):
        state.submission_type = 2

    if st.button("Profile match(%)🎯", help="Help you to find out your profile match in % with job description for the Job"):
        state.submission_type = 3

    if "submission_type" in state:
        progress_bar = st.progress(0)
        progress_message = st.empty()
        for percent_complete in range(101):
            progress_bar.progress(percent_complete)
            progress_message.text(f"Analysis Progress: {percent_complete}%")
            # Simulate some processing time
            time.sleep(0.03)
        progress_bar.empty()
        progress_message.empty()

        handle_submission(state.submission_type, input_text, uploaded_file)


def handle_submission(submission_type, input_text, uploaded_file):
    if uploaded_file is None:
        st.warning("Please upload the resume 📤")
        return

    pdf_content = input_pdf_setup(uploaded_file)
    if pdf_content is None:
        st.warning("Failed to process the uploaded PDF.❌")
        return

    input_prompts = {
    1: """
    You are a hiring manager with expertise in data science, full-stack web development, big data engineering, devops, or data analysis.
    Review the provided resume against the job description. Evaluate whether the candidate's profile aligns with the role.
    Provide your evaluation highlighting the candidate's strengths as "Your Strengths" and weaknesses as "Weaknesses" in relation to the specified job requirements.
    """,
    2: """
    Identify the missing keywords in the resume compared to the job description and list them as the missing skills in bullet points.
    """,
    3: """
    You are an experienced ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality.
    Evaluate the resume against the provided job description. Provide the percentage match if the resume aligns with the job description.
    Present the output in the following format: 
    - Percentage Match: [percentage]
    - Skills you already have: [matched keywords]
    - The skills that you miss: [missing keywords]
    - Final thoughts: [bullet points with candidate name and percentage match]
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
    page = st.sidebar.radio("Sections",["Home page 🏠" , "About the app 💻","Documentation 📒", "About the developer 👨‍💻"])
    if page == "Home page 🏠":
        about_app()
    elif page == "About the app 💻":
        about_the_app()
    elif page == "Documentation 📒":
        documentation()
    elif page == "About the developer 👨‍💻":
        about_developer()
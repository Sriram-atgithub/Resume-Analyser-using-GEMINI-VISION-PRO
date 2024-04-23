## Resume Analyser with Gemini Vision Pro
### This project is a web application designed to analyze resumes and provide insights for job seekers. It leverages the power of Google's Generative AI model, Gemini Vision Pro, to extract valuable information and identify strengths, weaknesses, and missing skills with a specific job description.

**Dependencies**
_Libraries:_
> - streamlit: Used for creating the interactive web application.
> - dotenv: Used for managing environment variables (API key).
> - genai: Interface to interact with Google GenerativeAI for Gemini Vision Pro.
> - pdf2image (Optional): Used for converting uploaded PDF resumes to images for processing by Gemini.
**External Services:**
> - Google GenerativeAI: Provides access to the Gemini Vision Pro model.

**Tech Stack**
- **Frontend:** _Streamlit_
- **Backend:** _Python_
- **Large Language Model:** _Google GenerativeAI (Gemini Vision Pro)_

**How the app works**
> ![Process Flow](https://github.com/Sriram-atgithub/ATS-Tracking-System-with-Gemini/blob/main/Flowchart.png)


**Advantages**
> **Automated Analysis:** Saves time and effort compared to manual resume review.
> **Data-Driven Insights:** Uses Gemini Vision Pro's understanding of the language for detailed analysis.
> **Actionable Feedback:** Identifies strengths, weaknesses, and missing skills to improve your resume and job candidacy.
> **User-Friendly Interface**: Streamlit provides a user-friendly platform for interaction.

**Limitations**

> **Model Dependence:** Relies on the accuracy and capabilities of Gemini Vision Pro.
> **Data Quality:** Relies on the provided job description and resume text quality.
> **Limited Context Understanding:** May not fully grasp the nuances and context of skills and experience, and it hallucinates.
> **Emerging Technology:** Large language models are still under development and might have limitations.

**Future Scope and Developments**
> **Skill Extraction and Matching:** Integrate libraries like spaCy or nltk for advanced skill extraction and matching between job description and resume.
> **Contextual Analysis:** Explore techniques like TF-IDF to analyze keywords' weightage within the job and resume context.
> **Feedback Loop and Model Improvement:** Implement user feedback mechanisms to improve the application's accuracy and effectiveness over time.
> **Multilingual Support:** Explore expanding the application to support resume and job description analysis in multiple languages.

_**About the Developer**_
This project was developed by **Sriram Ramakrishnan**. 
You can find more information about the developer through the following links:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sriram-aiexpert/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Sriram-atgithub)

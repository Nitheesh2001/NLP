import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Questions for the quiz with placeholders
questions = {
    "Teamwork": ("Please rate your teamwork skills from 1 to 5 and provide a brief example of a team project you have worked on.", "Rate from 1 to 5, and describe a team project"),
    "Problem Solving": ("Please rate your problem-solving skills from 1 to 5 and describe a situation where you solved a difficult problem.", "Rate from 1 to 5, and describe a problem-solving situation"),
    "Communication": ("Please rate your communication skills from 1 to 5 and share an experience where effective communication was crucial.", "Rate from 1 to 5, and describe a communication experience"),
    "Adaptability": ("Please rate your adaptability from 1 to 5 and give an example of how you adapted to a new situation.", "Rate from 1 to 5, and describe an adaptable situation"),
    "Critical Thinking": ("Please rate your critical thinking skills from 1 to 5 and provide an example of a time you used critical thinking.", "Rate from 1 to 5, and describe a critical thinking example"),
    "Time Management": ("Please rate your time management skills from 1 to 5 and describe how you manage your time effectively.", "Rate from 1 to 5, and describe time management strategies"),
    "Interpersonal": ("Please rate your interpersonal skills from 1 to 5 and share an example of how you interact with others in a professional setting.", "Rate from 1 to 5, and describe an interpersonal interaction")
}

# Function to get feedback from Gemini API
def get_feedback(answers):
    questions_and_answers = "\n".join([f"Q: {q}\nA: {a}" for q, a in answers.items()])
    prompt = f"""
    Based on the following self-assessment of soft skills, provide a detailed analysis and suggestions for improvement.
    {questions_and_answers}
    """
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

# Resources for improvement
resources = {
    "Teamwork": ["https://example.com/teamwork-video", "https://example.com/teamwork-document"],
    "Problem Solving": ["https://example.com/problem-solving-video", "https://example.com/problem-solving-document"],
    "Communication": ["https://example.com/communication-video", "https://example.com/communication-document"],
    "Adaptability": ["https://example.com/adaptability-video", "https://example.com/adaptability-document"],
    "Critical Thinking": ["https://example.com/critical-thinking-video", "https://example.com/critical-thinking-document"],
    "Time Management": ["https://example.com/time-management-video", "https://example.com/time-management-document"],
    "Interpersonal": ["https://example.com/interpersonal-video", "https://example.com/interpersonal-document"]
}

# Descriptions of why each skill is important
descriptions = {
    "Teamwork": "Teamwork is crucial for achieving collective goals, enhancing productivity, and fostering a collaborative environment.",
    "Problem Solving": "Problem-solving skills enable individuals to effectively tackle challenges and find innovative solutions.",
    "Communication": "Effective communication is essential for sharing information, building relationships, and ensuring clarity.",
    "Adaptability": "Adaptability helps individuals adjust to new circumstances, remain flexible, and thrive in changing environments.",
    "Critical Thinking": "Critical thinking involves analyzing situations, making informed decisions, and solving problems logically.",
    "Time Management": "Time management skills help prioritize tasks, meet deadlines, and maintain a healthy work-life balance.",
    "Interpersonal": "Interpersonal skills facilitate positive interactions, teamwork, and collaboration in professional settings."
}

# Streamlit app
st.set_page_config(page_title="Soft Skills Assessment", layout="wide")
st.title("Soft Skills Assessment")

# Collect user input
st.header("Answer the following questions to assess your soft skills")
answers = {}
for skill, (question, placeholder) in questions.items():
    answer = st.text_area(skill, placeholder=placeholder)
    answers[skill] = answer

# Button to submit the form
if st.button("Get Feedback"):
    if all(answers.values()):
        with st.spinner("Generating your soft skills assessment..."):
            try:
                feedback = get_feedback(answers)
                st.subheader("Your Soft Skills Feedback")
                st.write(feedback)
                
                # Display resources for improvement
                st.subheader("Resources for Improvement")
                for skill, answer in answers.items():
                    rating = int(answer.split()[0]) if answer.split() else 0
                    if rating < 4:  # Assuming a rating less than 4 indicates a need for improvement
                        st.markdown(f"### {skill}")
                        st.write(descriptions[skill])
                        for resource in resources[skill]:
                            st.write(resource)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please fill out all the fields.")

if __name__ == "__main__":
    st.sidebar.header("Soft Skills Assessment")

import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
import json

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Prompt template for skill gap analysis
prompt_template = """
You are an AI specializing in skill gap analysis. You will receive a list of skills required for a specific job 
and a list of skills the user currently possesses. Your task is to identify the skill gaps and suggest resources or 
courses to help the user acquire the missing skills. Provide the analysis in the following format:
{
  "Required Skills": ["skill1", "skill2", ...],
  "Current Skills": ["skillA", "skillB", ...],
  "Missing Skills": ["skillX", "skillY", ...],
  "Suggested Resources": [
    {
      "skill": "skillX",
      "resources": [
        {"name": "Resource 1", "link": "https://example.com/resource1"},
        {"name": "Resource 2", "link": "https://example.com/resource2"}
      ]
    },
    ...
  ]
}
"""

def generate_skill_gap_analysis(required_skills, current_skills):
    input_data = {
        "Required Skills": required_skills,
        "Current Skills": current_skills
    }
    prompt = prompt_template + str(input_data)
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text

def display_analysis_result(analysis_result):
    try:
        analysis_json = json.loads(analysis_result)
        
        st.subheader("Required Skills")
        st.write(", ".join(analysis_json["Required Skills"]))
        
        st.subheader("Current Skills")
        st.write(", ".join(analysis_json["Current Skills"]))
        
        st.subheader("Missing Skills")
        st.write(", ".join(analysis_json["Missing Skills"]))
        
        st.subheader("Suggested Resources")
        for resource in analysis_json["Suggested Resources"]:
            st.write(f"**{resource['skill']}**")
            for res in resource["resources"]:
                st.markdown(f"- [{res['name']}]({res['link']})")
    except Exception as e:
        st.error(f"Error parsing analysis result: {e}")

# Streamlit app
st.set_page_config(page_title="Skill Gap Analyzer", layout="wide")
st.title("Skill Gap Analyzer")
st.subheader("Identify and bridge your skill gaps")

st.markdown("### Enter the required and current skills to find out what you're missing and get suggestions to improve!")

required_skills = st.text_area("Enter the required skills for the job (comma-separated):", key="required_skills")
current_skills = st.text_area("Enter your current skills (comma-separated):", key="current_skills")

if st.button("Analyze Skill Gap"):
    if required_skills and current_skills:
        required_skills_list = [skill.strip() for skill in required_skills.split(",")]
        current_skills_list = [skill.strip() for skill in current_skills.split(",")]
        
        if not required_skills_list or not current_skills_list:
            st.warning("Please enter both required skills and current skills.")
        else:
            with st.spinner("Analyzing..."):
                try:
                    analysis_result = generate_skill_gap_analysis(required_skills_list, current_skills_list)
                    st.subheader("Skill Gap Analysis Result:")
                    display_analysis_result(analysis_result)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter both required skills and current skills.")

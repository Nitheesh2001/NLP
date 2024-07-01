1.field to put my job description
2. upload pdf or resume
3.pdf to image
4.promts template
5.multiple templates


# Smart ATS

Smart ATS is a Streamlit app that evaluates resumes against job descriptions using Google's Generative AI.

## Features

- Upload your resume (PDF)
- Paste a job description
- Get a percentage match, missing keywords, and profile summary

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/smart-ats.git
    cd smart-ats
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    Create a `.env` file with your Google API key:
    ```env
    GOOGLE_API_KEY=your_google_api_key
    ```

## Usage 

Start the application:
```bash
streamlit run app.py



## Project Structure

app.py: Main application code
requirements.txt: List of required Python libraries


# Requirements

streamlit
google-generativeai
python-dotenv
PyPDF2

# Example .env file

GOOGLE_API_KEY=your_google_api_key

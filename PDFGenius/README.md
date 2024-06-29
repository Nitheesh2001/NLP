PDFGenius 💁


Welcome to PDFGenius! This project allows you to interact with your PDF documents in a new and intelligent way. Upload your PDFs, ask questions, and get detailed, context-specific answers instantly.

Features
* Intelligent PDF Parsing: Extracts and processes text from multiple PDF documents seamlessly.
* Smart Text Chunking: Splits large texts into manageable chunks for efficient processing.
* Advanced Embeddings: Utilizes Google Generative AI Embeddings for high-quality vector representation.
* Conversational AI: Leverages ChatGoogleGenerativeAI to provide accurate and context-aware responses.
* Vector Store Integration: Employs FAISS for fast and effective similarity searches.
  
How It Works

1. Upload PDFs: Easily upload your PDF files through a user-friendly interface.
2. Ask Questions: Type in your questions related to the content of the PDFs.
3. Get Answers: Receive detailed and accurate answers based on the context from your uploaded documents.


Installation

To get started with PDFGenius, follow these steps:

1. Clone the repository: 

git clone https://github.com/Nitheesh2001/PDFGenius.git
cd PDFGenius

2. Create a virtual environment:
python -m venv venv

3. Activate the virtual environment:

On Windows:
venv\Scripts\activate

on macOS/Linux
source venv/bin/activate

4. Install the required packages:

pip install -r requirements.txt

5. Set up environment variables:
Create a .env file in the root directory of the project and add your Google API key:
GOOGLE_API_KEY=your_google_api_key_here



Usage
1. Run the Streamlit application:
streamlit run app.py


2. Open your web browser and go to http://localhost:8501 to access the PDFGenius interface.

3. Use the sidebar to upload your PDF files.

4. Type your questions in the text input field and get detailed answers based on the PDF content.



Code Overview


* app.py: Main application file. It contains the Streamlit app setup, PDF processing functions, and interaction logic.
* requirements.txt: List of all Python packages required to run PDFGenius.
* .env: Environment file for storing sensitive keys and configuration.

  
Dependencies

* Streamlit
* PyPDF2
* langchain
* langchain_google_genai
* google-generativeai
* FAISS
* dotenv

  
Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.



Contact
If you have any questions or feedback, feel free to reach out via LinkedIn or open an issue in this repository.
linkedin :www.linkedin.com/in/nitheeshm0123


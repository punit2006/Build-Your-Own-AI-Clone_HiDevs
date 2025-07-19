PDF Document Q&A and AI Chatbot
This Google Colab notebook provides a powerful solution for two distinct but related functionalities:

PDF Document Question Answering (Q&A): Upload any PDF document, and the system will extract its text, process it, and allow you to ask questions about its content.

General-Purpose AI Chatbot: Engage in a free-form conversation with an AI model capable of answering a wide range of questions, generating text, and more.

Both functionalities leverage the capabilities of Groq's Llama 3 70B model for fast and accurate responses, integrated via LangChain.

Features
PDF Text Extraction: Utilizes pypdf to extract text from your uploaded PDF documents.

Text Chunking: Employs RecursiveCharacterTextSplitter from LangChain to break down large texts into manageable chunks.

Vector Database Creation: Builds a local Chroma vector store using SentenceTransformerEmbeddings (all-MiniLM-L6-v2) for efficient semantic search.

Retrieval-Augmented Generation (RAG): Integrates the vector database with the Groq LLM to answer questions specifically based on the content of your PDF.

Interactive AI Chatbot: A simple command-line interface for general conversational AI.

Groq API Integration: Seamlessly connects to Groq's high-performance inference engine for LLM interactions.

Google Colab Secrets Management: Securely handles your API key using Colab's built-in userdata.get function.

Technologies Used
Python

LangChain: Framework for developing applications powered by language models.

Groq: High-speed inference engine for large language models.

ChromaDB: Lightweight, in-memory vector database.

Sentence Transformers: For generating embeddings (all-MiniLM-L6-v2).

PyPDF: For PDF text extraction.

Google Colab: Cloud-based Jupyter notebook environment.

Setup and Installation
Follow these steps to set up and run the notebook in Google Colab:

Open in Google Colab:

Go to Google Colab.

Click on File > Upload notebook and upload this .ipynb file.

Get your Groq API Key:

If you don't have one, sign up at Groq Cloud and generate a new API key.

Store API Key in Colab Secrets:

In your Google Colab notebook, click on the "🔑 Secrets" icon in the left sidebar.

Click + New secret.

For the Name, enter GROQ_API_KEY (it must be exactly this name).

For the Value, paste your Groq API key.

Ensure the "Notebook access" toggle is enabled for GROQ_API_KEY.

Install Dependencies:

Run the first cell in the notebook to install all required Python packages:

!pip install langchain chromadb sentence-transformers groq streamlit pypdf python-dotenv tqdm
!pip install -U langchain-community
!pip install langchain-groq

Load API Key and Initialize LLM:

Run the subsequent cells to load the GROQ_API_KEY and initialize the ChatGroq model. You should see "GROQ_API_KEY found in environment variables." and "ChatGroq model initialized." messages.

Usage
1. PDF Document Q&A
To use the PDF Q&A feature:

Upload Your PDF:

In the Colab environment, click on the "📁 Files" icon in the left sidebar.

Click on Upload to session storage icon (the first icon that looks like a file with an arrow pointing up) and upload your PDF file.

Important: Note the path where you upload it. For example, if you upload my_report.pdf directly to the content directory, its path will be /content/my_report.pdf.

Update pdf_path:

Locate the line pdf_path = r"/content/REPORTSAHIL.pdf" in the notebook.

Change "/content/REPORTSAHIL.pdf" to the actual path of your uploaded PDF file.

Run PDF Processing Cells:

Execute the cells under the "FOR PDF DATA EXTRACTION, HERE'S THE CODE ⬇" section. This will:

Extract text from your PDF.

Chunk the text.

Create and persist the Chroma vector database.

Initialize the RetrievalQA chain.

Ask Questions about the PDF:

The notebook includes example queries like query = "What does the pdf shows?" and query = "Provide a detailed description of the content of the PDF file.".

Run these cells to see the answers generated from your PDF's content. You can modify the query variable to ask your own questions.

2. General-Purpose AI Chatbot ("AI Clone")
To use the interactive AI Chatbot:

Run Chatbot Cells:

Execute the cells under the "HERE'S THE AI CLONE ⬇" section.

This will start an interactive prompt in your Colab output.

Start Chatting:

Type your questions or prompts into the input field and press Enter.

Type quit (case-insensitive) to exit the chat session.

Example interaction:

Enter your question (or type 'quit' to exit): What is the capital of France?
Question: What is the capital of France?
Answer: The capital of France is Paris.
------------------------------
Enter your question (or type 'quit' to exit): Write a short story about a cat.
Question: Write a short story about a cat.
Answer: [AI-generated short story]
------------------------------
Enter your question (or type 'quit' to exit): quit
Thank you for chatting! Goodbye.

Important Notes
API Key Security: Never hardcode your GROQ_API_KEY directly in the notebook or commit it to GitHub. Always use Colab Secrets or environment variables.

PDF File: Ensure the pdf_path variable correctly points to your uploaded PDF file for the Q&A functionality to work.

Model Choice: The notebook uses llama3-70b-8192 for ChatGroq. You can change this to other available Groq models if desired.

Ephemeral Storage: Files uploaded directly to Colab's session storage are temporary and will be lost when the runtime disconnects. If you need persistent storage for your PDFs, consider mounting Google Drive.

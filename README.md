# 🧠 PDF Document Q\&A & AI Chatbot

This Google Colab notebook provides a **powerful dual-purpose AI tool**:

* 📄 **PDF Document Q\&A**: Upload any PDF, extract its contents, and ask detailed questions about its contents.
* 💬 **General-Purpose AI Chatbot**: Engage in conversation with an AI chatbot powered by **Groq's LLaMA 3 70B model**.

> Both systems use **LangChain**, **Groq**, and **ChromaDB** to deliver fast, context-aware, and intelligent responses.

---

## 🚀 Features

| Functionality                | Description                                                                  |
| ---------------------------- | ---------------------------------------------------------------------------- |
| 📄 PDF Text Extraction       | Uses `pypdf` to extract readable text from PDF documents                     |
| ✂️ Text Chunking             | Utilizes `RecursiveCharacterTextSplitter` to break large text into chunks    |
| 🧠 Vector Store Creation     | Builds a local vector DB with `ChromaDB` and `SentenceTransformerEmbeddings` |
| 🔎 Retrieval-Augmented QA    | Queries answered using relevant PDF chunks + LLM (RAG architecture)          |
| 🤖 Interactive AI Chatbot    | Talk with an AI chatbot on any topic using a simple terminal interface       |
| ⚡ Groq LLM Integration       | Leverages the high-speed inference of **Groq's LLaMA 3 70B** model           |
| 🔐 Secure API Key Management | Uses **Google Colab Secrets** for secure key handling                        |

---

## 🛠️ Technologies Used

* **Python 3**
* [LangChain](https://www.langchain.com/)
* [Groq Cloud](https://console.groq.com/)
* [ChromaDB](https://www.trychroma.com/)
* [Sentence Transformers](https://www.sbert.net/)
* `pypdf`, `streamlit`, `tqdm`, `dotenv`, `Google Colab`

---

## ⚙️ Setup & Installation

### 🔗 Open in Google Colab

1. Go to [Google Colab](https://colab.research.google.com/).
2. Upload this `.ipynb` file using `File > Upload Notebook`.

### 🔑 Get Your Groq API Key

* Sign up at [Groq Cloud](https://console.groq.com/) and generate an API key.

### 🔒 Store API Key in Colab Secrets

1. Click the 🔐 **"Secrets"** icon in the Colab left sidebar.
2. Click `+ New secret`.
3. Set:

   * **Name**: `GROQ_API_KEY`
   * **Value**: Your Groq API Key
4. Ensure **Notebook Access** is enabled.

### 📦 Install Required Libraries

Run the following in the first code cell:

```bash
!pip install langchain chromadb sentence-transformers groq streamlit pypdf python-dotenv tqdm
!pip install -U langchain-community
!pip install langchain-groq
```

---

## 📄 PDF Q\&A Usage

### 1. Upload a PDF

* In Colab, click on the **📁 Files** tab.
* Upload your PDF file (e.g., `my_report.pdf`).
* Note its path: `/content/my_report.pdf`.

### 2. Update PDF Path

Update the line in the notebook:

```python
pdf_path = r"/content/my_report.pdf"  # <-- Change this to match your uploaded file
```

### 3. Run PDF Processing Cells

This will:

* Extract text from the PDF
* Chunk the text into vectors
* Store embeddings in ChromaDB
* Initialize the `RetrievalQA` pipeline

### 4. Ask Questions from the PDF

```python
query = "What is the summary of this report?"
result = qa_chain.run(query)
print("Answer:", result)
```

---

## 💬 General-Purpose AI Chatbot ("AI Clone")

### 1. Run Chatbot Section in Notebook

Start the chat loop:

```python
while True:
    query = input("Enter your question (or type 'quit' to exit): ")
    if query.lower() == "quit":
        print("Goodbye!")
        break
    response = llm.invoke(query)
    print("Answer:", response)
```

### 2. Example Chat

```
Enter your question: What is the capital of France?
Answer: The capital of France is Paris.

Enter your question: Write a story about a space cat.
Answer: [AI-generated story]

Enter your question: quit
Goodbye!
```

---

## 📝 Notes

* **Security**: Never hardcode your API keys in the notebook.
* **File Paths**: Ensure `pdf_path` points to the correct location of your PDF.
* **Persistence**: Colab file uploads are temporary. For persistence, mount Google Drive.
* **Model**: Default model used is `llama3-70b-8192`. You can switch models as needed.

---

## 📁 Folder Structure (Example)

```
.
├── pdf_qa_chatbot.ipynb         # Main Colab notebook
├── requirements.txt             # (Optional) Dependencies list
├── README.md                    # Project description and setup (this file)
```

---

## 🤝 Contribution

Feel free to fork, customize, or raise issues. Pull requests are welcome!

▶️ Run on Google Colab
Click the badge below to open and run this project in Google Colab:https://colab.research.google.com/drive/1Tke4BGDCAOSYrTdrJ7ThoMa0L1DYgNUf?usp=sharing

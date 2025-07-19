!pip install langchain chromadb sentence-transformers groq streamlit pypdf python-dotenv tqdm

import os

from google.colab import userdata



# Use Colab's Secrets manager to store your API key

# Click on the "🔑" icon in the left sidebar, add a new secret named GROQ_API_KEY

os.environ["GROQ_API_KEY"] = userdata.get('GROQ_API_KEY')



# You can optionally print to confirm it's loaded (be careful not to display the key itself)

# print("GROQ_API_KEY loaded.")

!pip install -U langchain-community

!pip install langchain-groq

from langchain_groq import ChatGroq

import os



groq_api_key = os.getenv("GROQ_API_KEY")



if not groq_api_key:

    print("Error: GROQ_API_KEY not found in environment variables. ChatGroq model not initialized.")

    llm = None

else:

    print("GROQ_API_KEY found in environment variables.")

    llm = ChatGroq(

        model="llama3-70b-8192",

        temperature=0,

        api_key=groq_api_key # Pass the key explicitly

    )

    print("ChatGroq model initialized.")



#FOR PDF DATA EXTRACTION, HERE'S THE CODE ⬇



JUST UPLOAD YOUR PDF AND COPY ITS PATH IN THE "pdf_path" AND THERE YOU GO.

from pypdf import PdfReader



# Replace 'your_document.pdf' with the actual path to your PDF file

pdf_path = r"/content/REPORTSAHIL.pdf"

raw_text = ''

try:

    reader = PdfReader(pdf_path)

    for page in reader.pages:

        raw_text += page.extract_text() + "\n"

    print("Text extracted successfully!")

except FileNotFoundError:

    print(f"Error: The file {pdf_path} was not found.")

except Exception as e:

    print(f"An error occurred: {e}")



# Now you can use this 'raw_text' in the subsequent steps of your QA system

# For example, you would use it when creating the Chroma vector DB:

# vectordb = Chroma.from_texts(chunks, embedding=embedding_model, persist_directory="chroma_store")



from langchain.text_splitter import RecursiveCharacterTextSplitter



text_splitter = RecursiveCharacterTextSplitter(

    chunk_size=1000,

    chunk_overlap=200

)

chunks = text_splitter.create_documents([raw_text])

print(f"Created {len(chunks)} chunks.")



from langchain_community.embeddings import SentenceTransformerEmbeddings



embedding_model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")



from langchain_community.vectorstores import Chroma



vectordb = Chroma.from_documents(

    documents=chunks,

    embedding=embedding_model,

    persist_directory="chroma_store"

)

print("Chroma vector database created and persisted.")



from langchain.chains import RetrievalQA



retriever = vectordb.as_retriever()



qa_chain = RetrievalQA.from_chain_type(

    llm=llm,

    retriever=retriever,

    chain_type="stuff"

)

print("RetrievalQA chain created.")



query = "What does the pdf shows?"

result = qa_chain.run(query)

print("\nAnswer:", result)

# Assuming qa_chain is already initialized from previous steps

if 'qa_chain' in locals() and qa_chain is not None:

    query = "Provide a detailed description of the content of the PDF file."

    try:

        result = qa_chain.run(query)

        print("\nDescription of the PDF file:", result)

    except Exception as e:

        print(f"An error occurred while getting the PDF description: {e}")

else:

    print("QA chain is not initialized. Please run the necessary cells to set up the QA chain.")



import os

from groq import Groq

from google.colab import userdata



# Load the API key from Colab Secrets

groq_api_key = userdata.get('GROQ_API_KEY')



if not groq_api_key:

    print("Error: GROQ_API_KEY not found in Colab Secrets.")

else:

    try:

        # Initialize the Groq client directly

        client = Groq(api_key=groq_api_key)



        # Make a simple API call to test authentication

        chat_completion = client.chat.completions.create(

            messages=[

                {

                    "role": "user",

                    "content": "Hello",

                }

            ],

            model="llama3-8b-8192", # Using a smaller, faster model for a quick test

        )



        print("Direct Groq API call successful!")

        print("Response:", chat_completion.choices[0].message.content)



    except Exception as e:

        print(f"Error during direct Groq API call: {e}")

        print("This error likely indicates an issue with the API key loaded from Secrets.")



#HERE'S THE AI CLONE ⬇



JUST ASK ANYHTING FROM WRITING THE CODE TO GET YOU A STORY, ANYTHING IN JUST ONE PROMPT

import os

from langchain_groq import ChatGroq

from google.colab import userdata

from datetime import datetime # Import datetime to get both date and time

from datetime import date # Still need date for date.today() if desired, but datetime.now() is sufficient



# Ensure GROQ_API_KEY is loaded from Secrets

groq_api_key = userdata.get('GROQ_API_KEY')



if not groq_api_key:

    print("Error: GROQ_API_KEY not found in Colab Secrets.")

    llm = None

else:

    # Initialize the ChatGroq model

    # You can choose a different model if available

    llm = ChatGroq(model="llama3-70b-8192", temperature=0, api_key=groq_api_key)

    print("ChatGroq model initialized.")



if llm:

    while True:

        # Ask a general question

        general_query = input("Enter your question (or type 'quit' to exit): ")



        if general_query.lower() == 'quit':

            print("Thank you for chatting! Goodbye.")

            break



        if general_query.strip(): # Only process if the query is not empty

            # Get current date and time

            now = datetime.now()

            date_time_info = f"Current date and time is {now}. "



            # Check if the query is a simple greeting (case-insensitive, leading/trailing spaces ignored)

            simple_greetings = ["hi", "hello", "hey"]

            if general_query.strip().lower() in simple_greetings:

                # If it's a simple greeting, send the original query without date/time

                prompt_to_send = general_query

            else:

                # For other queries, combine date/time info with the user's query

                prompt_to_send = date_time_info + general_query



            try:

                # Get the response from the model

                response = llm.invoke(prompt_to_send) # Use the constructed prompt



                print("\nQuestion:", general_query) # Print original question

                print("Answer:", response.content)

            except Exception as e:

                print(f"An error occurred during the API call: {e}")

        else:

            print("Please enter a question.")



        print("-" * 30) # Separator for clarity



else:

    print("LLM model not initialized due to missing API key. Cannot proceed.")

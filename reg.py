from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

loader = PyPDFLoader("C:\\Users\\Mughal\\Desktop\\cover.pdf")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = text_splitter.split_documents(documents)
print(f"Number of chunks loaded: {len(chunks)}")
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview",
                                          google_api_key="your api key")
vector_db = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory="./test_per")
print("PDF processed and saved to database!")

# 4. How to search (Retrieve)
query = "What is the main summary of this document?"
results = vector_db.similarity_search(query, k=2)

print(results[0].page_content)
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview",
                                          google_api_key="your api key")

# 2. Connect to the EXISTING database on your hard drive
# This loads it from the folder without re-reading the PDF
vector_db = Chroma(
    persist_directory="./test_per", 
    embedding_function=embeddings
)

# 3. Perform the search
query = "pakistan?" 
# here we can change the value of k as constant how much db search result we need 
results = vector_db.similarity_search(query, k=1)
collection = vector_db.get()


# 4. Display the results
for doc in results:
    print(doc.page_content)

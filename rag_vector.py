import pandas as pd
from tqdm import tqdm
from newspaper import Article
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

DB_FAISS_PATH = "vectorstores/db_faiss"

def extract_text_from_url(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        print(f"Error processing {url}: {e}")
        return None

def create_vector_db(urls):
    all_texts = []
    
    for url in tqdm(urls, desc="Processing URLs"):
        text = extract_text_from_url(url)
        if text:  # Ensure text is not None
            all_texts.append(text)

    if not all_texts:
        print("No valid text extracted. Exiting...")
        return

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_texts = []
    for text in all_texts:
        split_texts.extend(text_splitter.split_text(text))

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={'device': 'cpu'})

    db = FAISS.from_texts(split_texts, embeddings)
    db.save_local(DB_FAISS_PATH)
    print(f"Vector database saved at {DB_FAISS_PATH}")

if __name__ == '__main__':
    file_path = "input.xlsx"  
    df = pd.read_excel(file_path)
    
    if "URL" not in df.columns:
        print("No 'URL' column found in the Excel file. Exiting...")
    else:
        urls = df["URL"].dropna().tolist() 
        create_vector_db(urls)

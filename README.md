# **RAG-Based Chatbot for Blackcoffer**

## **Overview**
This chatbot leverages Retrieval-Augmented Generation (RAG) to provide AI-driven responses based on Blackcoffer's expertise. It extracts and processes textual data from URLs, stores embeddings in a FAISS vector database, and retrieves relevant information to answer user queries accurately using a language model.

## **How to Run**

### **Step 1: Generate the Vector Database**
Run the following command to extract text from URLs, create vector embeddings, and store them in FAISS:
```bash
python rag_vector.py
```

### **Step 2: Start the RAG Chatbot**
Once the vector database is generated, start the chatbot using Chainlit:
```bash
chainlit run chain.py
```


---
## Sample Output
![alt text](https://github.com/gaganchapa/rag_black_coffer/blob/main/bl.png)
![alt text](https://github.com/gaganchapa/rag_black_coffer/blob/main/bl2.png)
![alt text](https://github.com/gaganchapa/rag_black_coffer/blob/main/bl3.png)





# **Instructions Documentation**

## **Approach**
The script is designed to:
1. **Extract article text** from a list of URLs in `input.xlsx` using web scraping.
2. **Perform text analysis** on the extracted content, computing linguistic and sentiment-based metrics.

The solution is divided into two major steps:

### **1. Web Scraping (Extracting Article Text)**
- Reads `input.xlsx`, which contains a column named `URL`.
- Fetches the webpage content using `requests` and parses it with `BeautifulSoup`.
- Extracts the article title and body text using specific HTML tags.
- Saves the extracted content into `extracted_articles.csv`.

### **2. Text Analysis**
- Reads `extracted_articles.csv`.
- Cleans and tokenizes text while removing stopwords.
- Computes various linguistic metrics such as:
  - Sentiment scores (positive/negative polarity)
  - Readability scores (Fog Index, word/sentence length)
  - Word complexity, syllables, pronouns, etc.
- Saves the computed metrics in `text_analysis_results.csv`.

---

## **Dependencies**
Ensure you have the required dependencies installed before running the script.

```bash
pip install requests pandas beautifulsoup4 openpyxl nltk tqdm
```

---

## **How to Run**
1. **Prepare the Input File**
   - Place `input.xlsx` in the same directory as the script.
   - Ensure it has a column named `URL` with valid web links.

2. **Run the Script**
   ```bash
   python code_b.py
   ```
   This will:
   - Extract article text from the given URLs.
   - Perform linguistic analysis.
   - Generate two output files:
     - `extracted_articles.csv` (scraped content)
     - `text_analysis_results.csv` (computed metrics).

3. **Ensure Required Directories Exist**
   - A folder named `StopWords` should contain stopword text files.
   - A folder named `MasterDictionary` should have `positive-words.txt` and `negative-words.txt`.

---
## Sample Output
![alt text](https://github.com/gaganchapa/rag_black_coffer/blob/main/bl.png)
![alt text](https://github.com/gaganchapa/rag_black_coffer/blob/main/bl2.png)
![alt text](https://github.com/gaganchapa/rag_black_coffer/blob/main/bl3.png)





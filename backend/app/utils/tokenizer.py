import nltk
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup


nltk.download('punkt')
nltk.download('punkt_tab')

# def split_text_into_chunks(text, max_tokens=50):
#     words = word_tokenize(text)
#     print(words, 'words')
#     return [' '.join(words[i:i + max_tokens]) for i in range(0, len(words), max_tokens)]

def split_html_text_into_chunks(html: str, max_tokens=10):
    soup = BeautifulSoup(html, 'html.parser')
    
    for tag in soup(["script", "style", "noscript", "iframe"]):
        tag.decompose()

    allowed_attributes = ['class']
    for tag in soup.find_all():
        cleaned_attributes = {}

        for attribute, value in tag.attrs.items():
            if attribute in allowed_attributes:
                cleaned_attributes[attribute] = value

        tag.attrs = cleaned_attributes

    cleaned_html = soup.prettify()
    cleaned_soup = BeautifulSoup(cleaned_html, 'html.parser')
    blocks = cleaned_soup.find_all()
   

    chunks = []
    current_chunk_tokens = []
    current_chunk_html = ""

    for block in blocks:
        block_text = block.get_text(separator=" ", strip=True)
        block_html = str(block)
        block_tokens = word_tokenize(block_text)


        if len(current_chunk_tokens) + len(block_tokens) > max_tokens:
            if current_chunk_tokens:

                chunk_text = " ".join(current_chunk_tokens)
                chunks.append({
                    "cleaned_text": chunk_text,
                    "raw_html": current_chunk_html
                })

                current_chunk_tokens = []
                current_chunk_html = ""


        current_chunk_tokens.extend(block_tokens)
        current_chunk_html += block_html


    if current_chunk_tokens:
        chunk_text = " ".join(current_chunk_tokens)
        chunks.append({
            "cleaned_text": chunk_text,
            "raw_html": current_chunk_html
        })

    return chunks


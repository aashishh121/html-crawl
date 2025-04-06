from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize

def split_html_text_into_chunks(html: str, max_tokens=50):
    soup = BeautifulSoup(html, 'html.parser')

    for tag in soup(["script", "style", "noscript", "iframe"]):
        tag.decompose()

    blocks = soup.find_all()

    chunks = []

    for block in blocks:
        block_text = block.get_text(separator=" ", strip=True)
        block_html = str(block)
        block_tokens = word_tokenize(block_text)

        # If a block has too many tokens, split it
        if len(block_tokens) > 0:
            for i in range(0, len(block_tokens), max_tokens):
                chunk_tokens = block_tokens[i:i+max_tokens]
                chunk_text = " ".join(chunk_tokens)
                # Notice: we still use the same HTML for each sub-chunk

                chunks.append({
                    "cleaned_text": chunk_text,
                    "raw_html": block_html
                })

    return chunks

from fastapi import APIRouter

from app.models.search import SearchRequest
from app.services.search import fetch_html, insert_chunks_to_vectordb, search_chunks
from app.utils.tokenizer import split_html_text_into_chunks

router = APIRouter()

@router.post("/search")
async def search(request: SearchRequest):
    html = fetch_html(request.url)
    # cleaned = clean_html(html)
    # chunks = split_text_into_chunks(cleaned)
    chunks = split_html_text_into_chunks(html)
    insert_chunks_to_vectordb(chunks)
    results = search_chunks(request.query)
    return results

@router.get("/")
async def helloworld():
    return 'Hello world'


from pydantic import BaseModel

class SearchRequest(BaseModel):
    url: str
    query: str

class SearchResponse(BaseModel):
    content: str
    score: float

import requests
import weaviate
from app.core.vectordb import client
import weaviate
from weaviate import classes


def fetch_html(url: str) -> str:
    response = requests.get(url)
    # response.raise_for_status()
    if response.status_code != 200:
        raise Exception("Failed to fetch the URL")
    return response.text

# def clean_html(html: str) -> str:
#     soup = BeautifulSoup(html, 'html.parser')
#     for script in soup(["script", "style"]):
#         script.decompose()

#     return soup.get_text(separator=" ", strip=True)



def insert_chunks_to_vectordb(chunks):
    schema_name = "HtmlChunk"

    try:
        client.collections.get(schema_name)
    except weaviate.exceptions.WeaviateBaseError:
        client.collections.create(
            name=schema_name,
            properties=[
                classes.Property(name="content", data_type=classes.DataType.TEXT),
                 classes.Property(name="raw_html", data_type=classes.DataType.TEXT),
            ],
            vectorizer_config=classes.Configure.Vectorizer.text2vec_openai(),
        )
    
    # Add chunks to db
    collection = client.collections.get(schema_name)
    for chunk in chunks:
        collection.data.insert({
            "content": chunk["cleaned_text"],
            "raw_html": chunk["raw_html"]
        })


def search_chunks(query: str):
    collection = client.collections.get("HtmlChunk")

    result = collection.query.near_text(
        query=query,
        limit=10,
        include_vector = False,
        return_properties=["content","raw_html"],
        return_metadata=["certainty","distance", "score"],
    )

    unique_distances = set()
    unique_results = []

    for obj in result.objects:
        distance = obj.metadata.distance
        if distance is not None:
            rounded_distance = round(distance, 2) 
            if rounded_distance not in unique_distances:
                unique_distances.add(rounded_distance)
                unique_results.append(obj)

    return unique_results



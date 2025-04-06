import weaviate
from app.core.config import settings

client = weaviate.connect_to_local(
    host="localhost",
    port = 8080
)

if client.is_ready():
    print('weaviate connected')
else:
     print('weaviate not connected')
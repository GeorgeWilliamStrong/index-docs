from index_docs import (
    process_markdown_files,
    embed_text_and_store
)
import os

instill_api_key = os.environ.get("INSTILL_API_TOKEN")

print("Loading and splitting markdown files...")
chunks = process_markdown_files(
    "/Users/georgestrong/instill.tech",
    "/Users/georgestrong/",
    method='markdown',
    max_chunk_size=512,
    chunk_overlap=50
)

print("Embedding text and storing in Pinecone...")
embed_text_and_store(
    chunks,
    "doc_links",
    instill_api_key,
)

print("Indexing complete.")

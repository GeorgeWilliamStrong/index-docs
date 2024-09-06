import requests
import json
import logging
from concurrent.futures import ThreadPoolExecutor


def embedding_vdp(id, text, file_path, instill_api_key, pinecone_namespace):
    """
    Sends a POST request to the Instill API to trigger the embed-pinecone
    pipeline.

    VDP: https://instill.tech/george_strong/pipelines/index-pinecone

    Parameters
    ----------
    id : int
        The chunk ID.
    text : str
        The text to be processed.
    instill_api_key : str
        The API key for authentication.
    pinecone_namespace : str
        The namespace for the Pinecone index.

    Returns
    -------
    None

    """
    url = 'https://api.instill.tech/v1beta/users/george_strong/pipelines/\
index-semantic-search/trigger'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {instill_api_key}',
    }
    data = {
        "inputs": [
            {
                "chunk_id": f"{id}",
                "namespace": pinecone_namespace,
                "text_chunk": text.replace("\n", " ").replace('"', "'"),
                "doc_link": file_path,
            }
        ]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    logging.info(response.text)


def embed_text_and_store(chunks, pinecone_namespace, instill_api_key):
    """
    Embed a list of text chunks and store the embeddings in a file or vectorDB.

    Parameters
    ----------
    chunks : dict
        A dictionary containing all the text chunks. The keys are chunk IDs
        and the values are dictionaries with the keys 'chunk' (the text chunk)
        and 'file_path' (the path to the file the chunk came from).
    pinecone_namespace : str
        The name of the Pinecone namespace to use for storing the embeddings.
    instill_api_key : str
        The API key for the Instill API.

    Returns
    -------
    None
    """
    logging.basicConfig(
        filename="./data/indexing.log",
        level=logging.INFO,
        format='%(asctime)s %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p'
    )

    with ThreadPoolExecutor(max_workers=20) as executor:
        for id, chunk_data in chunks.items():
            executor.submit(embedding_vdp, id, chunk_data["chunk"],
                            chunk_data["file_path"], instill_api_key,
                            pinecone_namespace)

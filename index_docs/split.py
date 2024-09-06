from langchain.text_splitter import RecursiveCharacterTextSplitter, \
    MarkdownTextSplitter, TokenTextSplitter, TextSplitter
from .load import read_markdown_file, markdown_to_text, find_markdown_files
from .utils import remove_prefix, convert_to_link


def get_text_splitter(method: str, max_chunk_size:
                      int, chunk_overlap: int) -> TextSplitter:
    """
    Get a TextSplitter instance based on the specified method.

    Parameters
    ----------
    method : str
        The method to use for splitting text.
    max_chunk_size : int
        The maximum size of each chunk.
    chunk_overlap : int
        The overlap between adjacent chunks.

    Returns
    -------
    TextSplitter
        A TextSplitter instance.
    """
    if method == 'recursive_character':
        return RecursiveCharacterTextSplitter(chunk_size=max_chunk_size,
                                              chunk_overlap=chunk_overlap)
    elif method == 'markdown':
        return MarkdownTextSplitter(chunk_size=max_chunk_size,
                                    chunk_overlap=chunk_overlap)
    elif method == 'token':
        return TokenTextSplitter(chunk_size=max_chunk_size,
                                 chunk_overlap=chunk_overlap)
    else:
        raise ValueError(f"Unsupported splitter method: {method}")


def process_markdown_files(directory, prefix, method='markdown',
                           max_chunk_size=512, chunk_overlap=50):
    """
    Process all Markdown files in a directory, splitting their content into
    chunks. Only files within specific subdirectories ('docs', 'tutorials',
    'blog')
    are processed.

    Parameters
    ----------
    directory : str
        The directory containing Markdown files.
    prefix : str
        The prefix to remove from the file paths.
    method : str, optional
        The method to use for splitting text (default: 'markdown').
    max_chunk_size : int, optional
        The maximum size of each chunk (default: 512).
    chunk_overlap : int, optional
        The overlap between adjacent chunks (default: 50).

    Returns
    -------
    dict
        A dictionary containing all the text chunks. The keys are chunk IDs
        and the values are dictionaries with the keys 'chunk' (the text chunk)
        and 'file_path' (the path to the file the chunk came from).

    """
    all_chunks = {}
    splitter = get_text_splitter(method, max_chunk_size, chunk_overlap)
    markdown_files = find_markdown_files(directory)

    filtered_markdown_files = [file_path for file_path in markdown_files if
                               "instill.tech/docs/" in file_path or
                               "instill.tech/tutorials/" in file_path or
                               "instill.tech/blog/" in file_path]

    chunk_id = 0
    for file_path in filtered_markdown_files:
        markdown_content = read_markdown_file(file_path)
        text_content = markdown_to_text(markdown_content)
        chunks = splitter.split_text(text_content)

        file_path = remove_prefix(file_path, prefix)
        file_path = convert_to_link(file_path)

        for chunk in chunks:
            all_chunks[chunk_id] = {'chunk': chunk, 'file_path': file_path}
            chunk_id += 1

    return all_chunks

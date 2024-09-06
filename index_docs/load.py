import markdown
from bs4 import BeautifulSoup
import fnmatch
import os
import re


def find_markdown_files(root_dir):
    """
    Find all Markdown files in a directory, excluding those with "zh-CN" in the
    filename.

    Parameters
    ----------
    root_dir : str
        The root directory to search for Markdown files.

    Returns
    -------
    list of str
        The list of Markdown files found.
    """
    markdown_files = []
    for root, _, filenames in os.walk(root_dir):
        for filename in fnmatch.filter(filenames, '*.mdx'):
            if "zh-CN" not in filename:
                file_path = os.path.join(root, filename)
                markdown_files.append(file_path)

    return markdown_files


def read_markdown_file(file_path):
    """
    Read the content of a Markdown file.

    Parameters
    ----------
    file_path : str
        The path to the Markdown file.

    Returns
    -------
    str
        The content of the Markdown file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    return content


def markdown_to_text(markdown_content):
    """
    Convert Markdown content to plain text.

    Parameters
    ----------
    markdown_content : str
        The Markdown content to convert.

    Returns
    -------
    str
        The plain text content.
    """
    html_content = markdown.markdown(markdown_content)
    soup = BeautifulSoup(html_content, 'html.parser')
    text_content = soup.get_text()

    cleaned_text = re.sub(r'[^a-zA-Z0-9\s.,;:!?\'\"]', '', text_content)

    return cleaned_text

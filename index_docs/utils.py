def remove_prefix(path, prefix):
    """
    Remove a prefix from a path.

    Parameters
    ----------
    path : str
        The path to process.
    prefix : str
        The prefix to remove.

    Returns
    -------
    str
        The path with the prefix removed.
    """
    if path.startswith(prefix):
        return path[len(prefix):]

    return path


def convert_to_link(path):
    """
    Convert a path to a link.

    Parameters
    ----------
    path : str
        The path to convert.

    Returns
    -------
    str
        The converted link.
    """
    base_url = "https://www.instill.tech"
    if path.startswith('instill.tech'):
        link = path.replace('instill.tech', base_url)
        if link.endswith('.zh-CN.mdx'):
            link = link.replace('.zh-CN.mdx', '')
        elif link.endswith('.en.mdx'):
            link = link.replace('.en.mdx', '')
        elif link.endswith('.mdx'):
            link = link.replace('.mdx', '')
        return link
    else:
        return "Invalid path"

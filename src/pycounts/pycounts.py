import os
from collections import Counter
from string import punctuation


FilePathType = str | os.PathLike

def load_text(input_file: FilePathType) -> str:
    """Load text from a text file and return as a string

    Args:
        input_file (FilePathType): file path

    Returns:
        str: file content
    """
    with open(input_file, "r") as file:
        text = file.read()

    return text


def clean_text(text: str) -> str:
    """Lowercase and remove punctuation from a string.

    Args:
        text (str): file content

    Returns:
        str: cleaned file content
    """
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")
    return text


def count_words(input_file: FilePathType) -> Counter:
    """Count unique words in a string.

    Args:
        input_file (FilePathType): file path

    Returns:
        Counter: Counter dict-like
    """
    text = load_text(input_file)
    text = clean_text(text)
    words = text.split()
    return Counter(words)
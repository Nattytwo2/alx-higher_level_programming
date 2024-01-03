#!/usr/bin/python3
"""
text_indentation module
Function that prints a text with 2 new lines after some characters.

"""


def text_indentation(text):
    """
    Function prints a text with 2 new lines after each of these
    characters: ., ? and :.
    Args:
        text (str): First input.
    Raise: TypeError
    Return: New text.
    """
    if not type(text) in [str] or text is None or len(text) < 0:
        raise TypeError('text must be a string')
    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')
    print("\n".join([line.strip() for line in text.split("\n")]), end="")

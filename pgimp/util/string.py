def escape_single_quotes(string: str):
    """
    Escapes single quotes. Can be used when generating python code that places string contents into single quotes.

    Example:

    >>> print("print('{:s}')".format(escape_single_quotes("'")))
    print('\\'')

    :return:
    """
    return string.replace("'", "\\'")
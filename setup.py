from setuptools import setup, find_packages

setup (
    name = 'filemakerlexer',
    package = find_packages(),
    entry_points =
    """
    [pygments.lexers]
    filemakerlexer = filemakerlexer.lexer:FileMakerLexer
    """,
)

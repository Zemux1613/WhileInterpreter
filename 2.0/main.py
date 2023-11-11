import sys

from nltk import word_tokenize

from Parser import Parser
from Interpreter import Interpreter

if __name__ == "__main__":
    path = input("Welche Datei soll interpretiert werden? ")
    if not path:
        path = "../examples/add.while"

    if not path.endswith(".while"):
        print(f"Unter '{path}' ist keine Quellcode Datei.")
        sys.exit(-1)

    source_code = open(path, encoding="utf-8", mode="r").read()

    # lex to tokens
    tokenize_source = word_tokenize(source_code)
    print(tokenize_source)

    # syntax check
    statements = Parser(tokenize_source).parse()

    # create python code
    python_code = Interpreter(statements).generate_code()

    print(python_code)

    # execute python code
    # exec(python_code)

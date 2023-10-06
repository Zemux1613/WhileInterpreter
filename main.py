import sys
from Lexer import Lexer

from utils.FileUtil import *

if __name__ == "__main__":
    path = input("Welche Datei soll interpretiert werden? ")
    if not path:
        path = "examples/add.while"

    if not path.endswith(".while"):
        print(f"Unter '{path}' ist keine Quellcode Datei.")
        sys.exit(-1)

    source_code = FileUtil.read_file(FileUtil(), path)
    instructions = Lexer(source_code).lex()
    for instruction in instructions:
        print(str(instruction))
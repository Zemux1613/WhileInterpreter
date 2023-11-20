import sys

from nltk import word_tokenize

from Parser import Parser
from Interpreter import Interpreter

if __name__ == "__main__":
    path = input("Welche Datei soll interpretiert werden? ")
    if not path:
        path = "../examples/mul.while"

    if not path.endswith(".while"):
        print(f"Unter '{path}' ist keine Quellcode Datei.")
        sys.exit(-1)

    source_code = open(path, encoding="utf-8", mode="r").read()

    # lex to tokens
    tokenize_source = word_tokenize(source_code)
    # print(tokenize_source)

    # syntax check
    statements = Parser(tokenize_source).parse()

    # convert multi line statements into single instructions
    instructions = {}
    index = 0
    for keys in statements.keys():
        value = statements[keys]
        if ";" in value:
            value = value.replace("do", "do;")
            value_split = value.split(";")
            for statement in value_split:
                instructions[index] = statement.strip()
                index += 1
        else:
            instructions[index] = value.strip()
            index += 1

    # create python code
    python_code = Interpreter(instructions).generate_code()

    print(f"Sourcecode: \n'{python_code}'\n\npossible programm output:")

    # execute python code
    exec(python_code)

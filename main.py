import nltk
from nltk import word_tokenize, CFG
import sys
import re
import StatementCollectorExtention as sce
from Interpreter import Interpreter


def parse_input(parser, tokens, debug=False):
    try:
        if debug:
            parser._trace = 3
        for tree in parser.parse(tokens):
            if debug:
                print(tree)
                tree.pretty_print()
                # tree.draw()
            return True
    except nltk.EarleyChartParser.NotParseable:
        pass
    finally:
        if debug:
            parser._trace = 0
    return False


if __name__ == "__main__":

    debug_str = "False"  # input("Debugger aktivieren? (True/False) ")

    while not re.match(r"(True|False)", debug_str):
        debug_str = input("Ungültige Eingabe! Debugger aktivieren? ")

    debug = bool(debug_str)

    path = input("Welche Datei soll interpretiert werden? ")
    if not path:
        path = "./examples/list.while"

    if not path.endswith(".while"):
        print(f"Unter '{path}' ist keine Quellcode Datei.")
        sys.exit(-1)

    source_code = open(path, encoding="utf-8", mode="r").read()

    # lex to tokens
    tokenize_source = word_tokenize(source_code)

    keywords = ["=", "!", "do", "while", "end", "print", ";"]

    for index in range(len(tokenize_source)):
        token = tokenize_source[index]
        if not token in keywords:
            if re.match("([0-9])", token):
                tokenize_source[index] = 'num'
            elif re.match("([a-z])", token):
                tokenize_source[index] = 'var'

    grammar = CFG.fromstring("""
        programm -> 'var' '=' 'var' operator 'num' 
        programm -> 'var' '+=' 'num'
        programm -> programm ';' programm
        programm -> 'while' 'var' '!' '=' 'num' 'do' programm 'end'
        programm -> 'print' 'var'
        operator -> '+' | '-'
    """)

    # Erstellen Sie einen Parser basierend auf der Grammatik
    parser = nltk.EarleyChartParser(grammar=grammar)

    parsed = parse_input(parser, tokenize_source, debug)
    print(f"parse: {parsed}")
    if not parsed:
        print("Syntax Error!")
    else:
        statements = sce.StatementCollectorExtention(word_tokenize(source_code)).summarize_statements()
        generate_code = Interpreter(statements).generate_code()

        # code pre-view
        print(f"\n{generate_code.strip()}\n\nProgramm output:\n")

        # execute code
        exec(generate_code)

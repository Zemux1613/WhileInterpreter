import nltk
from nltk import word_tokenize, CFG
import sys
import re
import StatementCollectorExtention as sce


def parse_input(parser, tokens, debug=False):
    try:
        if debug:
            parser._trace = 3
        # Versuche, den Parser auf die Eingabe anzuwenden
        for tree in parser.parse(tokens):
            # Wenn es mindestens einen Parse-Baum gibt, ist die Syntax korrekt
            if debug:
                print(tree)
                tree.pretty_print()
                tree.draw()
            return True
    except nltk.EarleyChartParser.NotParseable:
        # Wenn eine NotParseable-Ausnahme ausgelöst wird, ist die Syntax nicht korrekt
        pass
    finally:
        # Deaktiviere den Debug-Modus des Parsers nach dem Parsen
        if debug:
            parser._trace = 0
    return False


if __name__ == "__main__":

    debug_str = "False" # input("Debugger aktivieren? ")

    while not re.match("(True|False)", debug_str):
        debug_str = input("Ungültige Eingabe! Debugger aktivieren? ")

    debug = bool(debug_str)

    path = ""  # input("Welche Datei soll interpretiert werden? ")
    if not path:
        path = "./examples/loop_stack.while"

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
        programm -> programm ';' programm
        programm -> 'while' 'var' '!' '=' 'num' 'do' programm 'end'
        programm -> 'print' 'var'
        operator -> '+' | '-'
    """)

    # Erstellen Sie einen Parser basierend auf der Grammatik
    parser = nltk.EarleyChartParser(grammar=grammar)

    parsed = parse_input(parser, tokenize_source, False)
    print(f"parse: {parsed}")

    if parsed:
        statements = sce.StatementCollectorExtention(word_tokenize(source_code)).summarize_statements()
        generate_code = sce.StatementCollectorExtention.generate_code(sce.Interpreter(statements))

        print(f'{generate_code}')

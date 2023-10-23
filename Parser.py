import sys


class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.top = None
        # init cellar
        self.cellar = []
        self.cellar.append("|")
        self.cellar.append("s")

    def next_token(self):
        print(f"Tokens: {[token.identifier for token in self.tokens]}")
        print(f"Cellar: {[top for top in self.cellar]}")
        if not self.tokens or len(self.tokens) == 0:
            return None
        self.top = self.tokens.pop(0)
        return self.top

    def parse(self):

        self.next_token()

        next_token = self.top

        print(f"Token: {next_token.get_identifier()} - {next_token.get_value()}")

        if next_token is None:
            cellar_top = self.cellar.pop()

            if not cellar_top == "|":
                sys.exit(f"Invalid Syntax: {self.cellar}")

        if "operator" == next_token.get_identifier():
            cellar_top = self.cellar.pop()
            next_item = self.cellar.pop()

            if cellar_top == "operator" and next_item == "i":
                self.cellar.append(next_item)
                self.parse()
                return
            else:
                self.invalid_syntax(next_token)

        if ":=" == next_token.get_identifier():
            cellar_top = self.cellar.pop()
            next_item = self.cellar.pop()

            if cellar_top == "n=" and next_item == "nx":
                self.cellar.append(next_item)
                self.parse()
                return
            else:
                self.invalid_syntax(next_token)

        if "num" == next_token.get_identifier():
            cellar_top = self.cellar.pop()
            next_item = self.cellar.pop()

            if cellar_top == "i" and (next_item == "n=" or next_item == "operator" or next_item == "|"):
                self.cellar.append(next_item)
                self.parse()
                return
            else:
                self.invalid_syntax(next_token)

        if "x" == next_token.get_identifier():
            cellar_top = self.cellar.pop()
            if cellar_top == "s":
                self.cellar.append("i")
                self.cellar.append("operator")
                self.cellar.append("i")
                self.cellar.append("nx")
                self.cellar.append("n=")
                self.cellar.append("i")
                self.parse()
                return

            next_item = self.cellar.pop()
            if cellar_top == "nx" and next_item == "i":
                self.cellar.append("i")
                self.parse()
                return

            self.invalid_syntax(next_token)

    def invalid_syntax(self, next_token):
        sys.exit(f"Invalid Syntax: {next_token.get_identifier()} - {next_token.get_value()}")

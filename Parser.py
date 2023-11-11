import re


class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def consume(self, token, regex=False):
        print(f"trying to consume '{token}'")
        print(f"regex='{regex}', token='{self.tokens[self.position]}'")
        if (not regex and self.tokens[self.position] == token) or (
                regex and re.search(token, self.tokens[self.position])):
            print(f"consume {token}")
            self.position += 1
        else:
            raise Exception(f"invalid syntax error! '{token}' isn't on position {self.position}")

    def assignment(self):
        self.variable()
        self.consume(":=")
        self.operator()
        self.atom()

    def operator(self):
        if self.tokens[self.position] == '+' or self.tokens[self.position] == '-':
            self.consume(self.tokens[self.position], False)

    # An atom is a variable or a number
    def atom(self):
        self.consume("([a-z]{1,}|[0-9]{1,})", True)

    def variable(self):
        self.consume("([a-z]+)", True)

    def statement(self):
        statement = None
        try:
            statement = self.assignment()
        except Exception as ex:
            pass

        return statement

    def programm(self):
        statement = self.statement()
        return statement

    def parse(self):
        statement = self.programm()

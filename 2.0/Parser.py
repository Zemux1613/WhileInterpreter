import re


class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def consume(self, pattern):
        print(f"trying to consume token={self.tokens[self.position]}, patter='{pattern}', position={self.position}, tokens={self.tokens[self.position:]}")
        if re.match(pattern, self.tokens[self.position]):
            print(f"consume {pattern}")
            self.position += 1
        else:
            raise Exception(f"invalid syntax, token {self.tokens[self.position]} didn't macht with '{pattern}'")

    def programm(self):
        # first statement is required
        first_statement = self.statement()

        # indexing statements
        index = 0

        statements = {index: first_statement}

        # other statements are optional
        while ";" in self.tokens[self.position:]:
            self.consume(r"(;)")
            statement = self.statement()
            index += 1
            statements[index] = statement

        return statements

    def statement(self):
        statement = None
        start = self.position
        try:
            statement = self.assignment()
        except Exception as ex:
            self.position = start
            try:
                statement = self.print()
            except Exception as ex1:
                self.position = start
                try:
                    statement = self.loop()
                except Exception as ex2:
                    self.position = start
        return statement

    def print(self):
        start = self.position
        self.consume("(print)")
        self.variable()
        return ' '.join(self.tokens[start:self.position])

    def assignment(self):
        start = self.position
        self.variable()
        self.consume(r"(=)")
        self.variable()
        self.operator()
        self.number()
        return ' '.join(self.tokens[start:self.position])

    def number(self):
        self.consume(r"([0-9]+)")

    def operator(self):
        self.consume(r"(\+|-)")

    def variable(self):
        self.consume(r"([a-z]+)")

    def parse(self):
        return self.programm()

    def loop(self):
        start = self.position
        self.consume(r"(while)")
        self.variable()
        self.consume(r"(!)")
        self.consume(r"(=)")
        self.number()
        self.consume(r"(do)")
        self.programm()
        self.consume(r"(end)")
        return ' '.join(self.tokens[start:self.position])

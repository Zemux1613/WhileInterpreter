import re


class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def consume(self, pattern):
        print(
            f"trying to consume token={self.tokens[self.position]}, patter='{pattern}', position={self.position}, tokens={self.tokens[self.position:]}")
        if re.match(pattern, self.tokens[self.position]):
            print(f"consume {pattern}")
            self.position += 1
        else:
            raise Exception(f"invalid syntax, token {self.tokens[self.position]} didn't macht with '{pattern}'")

    def programm(self):
        # first statement is required
        first_statement = self.statement()

        statements = [first_statement]

        # other statements are optional
        while ";" in self.tokens[self.position:]:
            self.consume("(;)")
            statement = self.statement()
            statements.append(statement)

        return statements

    def statement(self):
        statement = None
        start = self.position
        try:
            statement = self.assignment()
        except Exception as ex:
            self.position = start
            try:
                statement = self.loop()
            except Exception as ex1:
                self.position = start
        return statement

    def assignment(self):
        start = self.position
        self.variable()
        self.consume("(=)")
        self.variable()
        self.operator()
        self.number()
        return ' '.join(self.tokens[start:self.position])

    def number(self):
        self.consume("([0-9]+)")

    def operator(self):
        self.consume("(\+|-)")

    def variable(self):
        self.consume("([a-z]+)")

    def parse(self):
        return self.programm()

    def loop(self):
        start = self.position
        self.consume("(while)")
        self.variable()
        self.consume("(!)")
        self.consume("(=)")
        self.number()
        self.consume("(do)")
        self.programm()
        self.consume("(end)")
        return ' '.join(self.tokens[start:self.position])

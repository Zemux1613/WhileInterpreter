import re
import sys
from enum import Enum


class Lexer:

    def __init__(self, content):
        self.content = content
        self.lines = content.split("\n")
        self.instructions = []

    def lex(self):
        for i in range(0, len(self.lines), 1):
            line = self.lines[i]

            # ignore empty lines
            if (len(line) == 0) or (not line):
                continue

            line = line.strip()

            # ignore commented lines
            if line.startswith(";"):
                continue

            if ";" in line:
                line = line[0:line.index(";")]

            token = None

            for t in Token.all():
                if re.match(t.get_identifier(), line.strip()):
                    token = t
                    break

            if token is None:
                print(f"Invalid line: '{line}'")
                sys.exit(i)

            self.instructions.append(Instruction(i + 1, token))

        return self.instructions

    def get_instructions(self):
        return self.instructions


class Token(Enum):
    ASSIGNMENT = r"([a-zA-Z]+[0-9]*\s*:=\s*[a-zA-Z]+[0-9]*\s*(\+|-)\s*[0-9]+)", False
    PRINT = r"(print\s*[a-zA-Z]+[0-9]*)", False
    WHILE = r"(while)", True
    END = r"(end)", False

    def __init__(self, identifier, multi_line):
        self.identifier = identifier
        self.multi_line = multi_line

    def get_identifier(self):
        return self.identifier

    def get_multi_line(self):
        return self.multi_line

    @classmethod
    def all(cls):
        return [getattr(cls, attr) for attr in cls.__members__]


class Instruction:
    def __init__(self, line, token):
        self.line = line
        self.token = token

    def get_token(self):
        return self.token

    def get_line(self):
        return self.line

    def __str__(self):
        return f'{self.line}: {self.token.name}'


class MultilineInstruction(Instruction):
    def __init__(self, line, token, instructions):
        super().__init__(line, token)
        self.instructions = instructions

    def get_instructions(self):
        return self.instructions

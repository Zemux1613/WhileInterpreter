import re

class Lexer:

    def __init__(self, content):
        self.content = content
        self.lines = content.split("\n")
        self.tokens = []

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

            for word in re.sub(r'([a-zA-Z]+(\d+))', r'x \2', line).split():
                tokenized_word = word

                tokenized_word = re.sub(r"([0-9])+", "num", tokenized_word)
                tokenized_word = re.sub(r"(\+|-)+", "operator", tokenized_word)

                token = Token(tokenized_word, word)

                self.tokens.append(token)

        return self.tokens

    def get_tokens(self):
        return self.tokens


class Token:
    def __init__(self, identifier, value):
        self.identifier = identifier
        self.value = value

    def get_identifier(self):
        return self.identifier

    def get_value(self):
        return self.value

    def __str__(self):
        return f"{self.identifier}: {self.value}"

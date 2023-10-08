import sys

import Lexer


class Parser:

    def __init__(self, instructions):
        self.instructions = instructions
        self.program = []
        self.top = None
        self.multi_line_statement = []

    def next_instruction(self):
        self.top = self.instructions.pop()
        return self.top

    def parse(self):

        while self.instructions:

            self.next_instruction()

            print(self.top.get_token())

            if not self.multi_line_statement:
                if Lexer.Token.END == self.top:
                    self.multi_line_statement.append(self.top)
                    self.program.append(self.multi_line_statement)
                    self.multi_line_statement.clear()
                    continue
                elif Lexer.Token.ASSIGNMENT == self.top.get_token() or Lexer.Token.PRINT == self.top.get_token:
                    self.multi_line_statement.append(self.top)
                    continue

            elif Lexer.Token.ASSIGNMENT == self.top.get_token() or Lexer.Token.PRINT == self.top.get_token:
                self.program.append(self.top)

            elif Lexer.Token.WHILE == self.top.get_token():
                self.multi_line_statement.append(self.top)

            else:
                sys.exit(f"Invalid syntax in line {self.top.get_line()} \n {str(self.top.get_token)}")

        return self.program

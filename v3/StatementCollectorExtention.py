from v2.Interpreter import Interpreter

class StatementCollectorExtention(Interpreter):

    def __init__(self, tokens):
        self.tokens = tokens

    def summarize_statements(self):
        statements = []
        pos = 0

        while ";" in self.tokens[pos:]:
            index = self.tokens[pos:].index(";")

            join = ' '.join(self.tokens[pos:pos + index])
            if "while" in join:
                join_split = join.split("do")
                statements.append(join_split[0] + " do")
                statements.append(join_split[1])
            elif "end" in join:
                join_split = join.split("end")
                statements.append(join_split[0])
                statements.append("end")
            else:
                statements.append(join)

            pos = pos + index + 1

        self.statements = statements
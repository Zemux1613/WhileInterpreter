class Interpreter:

    def __init__(self, statements):
        self.statements = statements

    def generate_code(self):
        source_code = ""
        for statement in self.statements:
            # while loop
            if statement.startswith("while"):
                pass
            # assignment statement
            elif "+" in statement or "-" in statement:
                operator = "+" if "+" in statement else "-"
                line = ""
                lhs, rhs_operator = map(str.strip, statement.split("="))
                rhs, remainder = map(str.strip, rhs_operator.split(operator, 1))

                if lhs == rhs:
                    line = f"{lhs} {operator}= {remainder}"
                else:
                    line = statement

                source_code += f"{line}\n"

        return source_code
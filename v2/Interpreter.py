class Interpreter:

    def __init__(self, statements):
        self.statements = statements

    def format_code(self, source_code):
        depth = 0
        formated_source_code = ""
        for line in source_code.split("\n"):
            prefix = ""
            for i in range(depth):
                prefix += "\t"
            if "while" in line:
                depth += 1
            if "end" in line:
                depth -= 1
                line = line.replace("end", "")
            formated_source_code += prefix + line + "\n"

        return formated_source_code

    def generate_code(self):
        source_code = ""
        for statement in self.statements.values():
            # print variable
            if statement.startswith("print"):
                source_code += f"print({statement.replace('print', '').strip()})\n"

            # end loop
            if statement.startswith("end"):
                source_code += statement

            # while loop
            if statement.startswith("while"):
                if "! =" in statement:
                    statement = statement.replace("! =", "!=")
                source_code += f"{statement.replace('do', ':')}\n"

            # assignment statement
            elif "+" in statement or "-" in statement:
                operator = "+" if "+" in statement else "-"
                line = ""
                lhs, rhs_operator = map(str.strip, statement.split("="))
                rhs, remainder = map(str.strip, rhs_operator.split(operator, 1))

                declaration = False

                variable_declaration = lhs + " = "
                if variable_declaration not in source_code:
                    declaration = True

                if not declaration:
                    if lhs == rhs:
                        line = f"{lhs} {operator}= {remainder}"
                    else:
                        line = statement
                else:
                    line = f"{lhs} = {remainder}"

                source_code += f"{line}\n"

        return self.format_code(source_code)

import ast

class ASTParser:
    @staticmethod
    def parse_code(source_code):
        try:
            return ast.parse(source_code)
        except SyntaxError as e:
            print(f"Syntax error in source code: {e}")
            return None

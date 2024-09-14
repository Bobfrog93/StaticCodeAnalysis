import ast
from reports.report import Report

class FunctionLengthRule:
    def __init__(self, max_lines=10):
        self.max_lines = max_lines

    def apply(self, ast_tree, file_name, report_generator):
        for node in ast.walk(ast_tree):
            if isinstance(node, ast.FunctionDef):
                function_length = (node.end_lineno or 0) - (node.lineno or 0) + 1
                if function_length > self.max_lines:
                    warning_message = f"Function '{node.name}' is too long ({function_length} lines)."
                    print(warning_message)

                    # Generate report and add to report generator
                    report = Report(file_name=file_name, rule_type="function_length", message=warning_message, line_number=node.lineno)
                    report_generator.add_report(report)

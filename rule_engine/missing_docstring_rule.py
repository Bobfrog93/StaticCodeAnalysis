import ast
from reports.report import Report

class MissingDocstringRule:
    def apply(self, ast_tree, file_name, report_generator):
        for node in ast.walk(ast_tree):
            if isinstance(node, ast.FunctionDef):
                docstring = ast.get_docstring(node)
                if docstring is None or not docstring.strip():
                    warning_message = f"Warning: Function '{node.name}' is missing a docstring."
                    print(warning_message)

                    # Generate report and add to report generator
                    report = Report(file_name=file_name, rule_type="missing_docstring", message=warning_message, line_number=node.lineno)
                    report_generator.add_report(report)

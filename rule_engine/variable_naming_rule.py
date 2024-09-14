import ast
from reports.report import Report

class VariableNamingConventionRule:
    def apply(self, ast_tree, file_name, report_generator):
        builtins = dir(__builtins__)
        for node in ast.walk(ast_tree):
            if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
                if not node.id.islower() and not node.id.isupper():
                    if node.id not in builtins:
                        warning_message = f"Variable '{node.id}' does not follow snake_case naming convention."
                        print(warning_message)

                        # Generate report and add to report generator
                        report = Report(file_name=file_name, rule_type="variable_naming_convention", message=warning_message, line_number=node.lineno)
                        report_generator.add_report(report)

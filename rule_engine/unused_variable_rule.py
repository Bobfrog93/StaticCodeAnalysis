import ast
from reports.report import Report

class UnusedVariableRule:
    def apply(self, ast_tree, file_name, report_generator):
        assigned_vars = set()
        used_vars = set()
        builtins = dir(__builtins__)

        for node in ast.walk(ast_tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and isinstance(target.ctx, ast.Store):
                        assigned_vars.add(target.id)

            if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
                used_vars.add(node.id)

        unused_vars = assigned_vars - used_vars - set(builtins)
        for var in unused_vars:
            warning_message = f"Variable '{var}' is assigned but never used."
            print(warning_message)

            # Generate report and add to report generator
            report = Report(file_name=file_name, rule_type="unused_variable", message=warning_message)
            report_generator.add_report(report)

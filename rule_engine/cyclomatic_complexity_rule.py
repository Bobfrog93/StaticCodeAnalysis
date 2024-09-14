import ast
from reports.report import Report

class CyclomaticComplexityRule:
    def __init__(self, threshold=5):
        self.threshold = threshold

    def apply(self, ast_tree, file_name, report_generator):
        def calculate_complexity(node, depth=0):
            complexity = 1 if depth == 0 else 0
            for child in ast.iter_child_nodes(node):
                if isinstance(child, (ast.For, ast.While, ast.ExceptHandler)):
                    complexity += 1
                elif isinstance(child, ast.If):
                    complexity += 1
                    if child.orelse:
                        complexity += 1
                elif isinstance(child, ast.BoolOp):
                    complexity += len(child.values) - 1

                if not isinstance(child, ast.FunctionDef):
                    child_complexity = calculate_complexity(child, depth + 1)
                    complexity += child_complexity
            return complexity

        for node in ast.walk(ast_tree):
            if isinstance(node, ast.FunctionDef):
                complexity = calculate_complexity(node)
                if complexity > self.threshold:
                    warning_message = f"Function '{node.name}' has high cyclomatic complexity ({complexity})."
                    print(warning_message)

                    # Generate report and add to report generator
                    report = Report(file_name=file_name, rule_type="cyclomatic_complexity", message=warning_message, line_number=node.lineno)
                    report_generator.add_report(report)

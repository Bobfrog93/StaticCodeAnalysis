from reports.report import Report

class RuleExecutor:
    def __init__(self, report_generator, file_name):
        self.report_generator = report_generator
        self.file_name = file_name

    def execute_rule(self, rule, ast_tree):
        try:
            # Apply the rule and pass the file_name and report_generator
            rule.apply(ast_tree, self.file_name, self.report_generator)
        except Exception as e:
            # Handle any exceptions and generate an error report
            error_message = f"Rule '{rule.__class__.__name__}' encountered an error: {str(e)}"
            print(error_message)
            report = Report(file_name=self.file_name, rule_type=rule.__class__.__name__, message=error_message)
            self.report_generator.add_report(report)

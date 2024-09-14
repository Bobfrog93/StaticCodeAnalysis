import importlib
import os
from rule_engine.rule_executor import RuleExecutor

class DynamicRuleManager:
    def __init__(self, rule_directory):
        self.rules = []
        self.load_rules(rule_directory)

    def load_rules(self, rule_directory):
        # Dynamically load all rules in the rule_engine folder
        for file in os.listdir(rule_directory):
            if file.endswith('_rule.py') and file != '__init__.py':
                module_name = file[:-3]  # Remove '.py'
                try:
                    rule_module = importlib.import_module(f'rule_engine.{module_name}')
                    rule_class_name = module_name.replace('_', ' ').title().replace(' ', '')
                    rule_class = getattr(rule_module, rule_class_name)
                    self.rules.append(rule_class())
                except (ImportError, AttributeError) as e:
                    print(f"Error loading rule: {file} - {e}")

    def apply_rules(self, ast_tree, file_name, report_generator):
        # Use RuleExecutor to wrap rule execution
        rule_executor = RuleExecutor(report_generator, file_name)
        for rule in self.rules:
            rule_executor.execute_rule(rule, ast_tree)

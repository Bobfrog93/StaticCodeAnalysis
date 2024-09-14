import os
import concurrent.futures
from parsers.python_parser import ASTParser
from rule_engine.rule_manager import DynamicRuleManager
from reports.report_generator import JSONReportGenerator
from reports.report import Report

def analyze_file(file_path):
    with open(file_path, 'r') as file:
        source_code = file.read()

    # Parse the code into an AST
    ast_tree = ASTParser.parse_code(source_code)
    if ast_tree is None:
        return []

    # Initialize the rule manager and apply rules
    rule_manager = DynamicRuleManager('rule_engine')
    file_name = os.path.basename(file_path)
    
    # Create a local report generator for this file
    local_report_generator = JSONReportGenerator()
    
    rule_manager.apply_rules(ast_tree, file_name, local_report_generator)
    
    # Return the reports for this file
    return local_report_generator.reports

def main():
    # Get all Python files from the 'tests' directory
    file_paths = [os.path.join('tests', f) for f in os.listdir('tests') if f.endswith('.py')]

    # Run the analysis in parallel
    with concurrent.futures.ProcessPoolExecutor() as executor:
        all_reports = list(executor.map(analyze_file, file_paths))

    # Flatten the list of reports
    flattened_reports = [report for file_reports in all_reports for report in file_reports]

    # Create the final report generator and add all reports
    final_report_generator = JSONReportGenerator()
    for report_dict in flattened_reports:
        report = Report(**report_dict)
        final_report_generator.add_report(report)

    # Generate the report
    final_report_generator.generate()

if __name__ == "__main__":
    main()

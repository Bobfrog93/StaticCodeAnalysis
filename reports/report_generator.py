import json

class JSONReportGenerator:
    def __init__(self):
        self.reports = []

    def add_report(self, report):
        # Add a report object to the list
        self.reports.append(report.to_dict())

    def generate(self, filename='report.json'):
        # Output all reports as a JSON file
        with open(filename, 'w') as report_file:
            json.dump(self.reports, report_file, indent=4)

    def print_report(self):
        # For debugging, print all reports
        for report in self.reports:
            print(report)

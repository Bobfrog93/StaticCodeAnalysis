class Report:
    def __init__(self, file_name, rule_type, message, line_number=None):
        self.file_name = file_name
        self.rule_type = rule_type
        self.message = message
        self.line_number = line_number

    def to_dict(self):
        report = {
            "file_name": self.file_name,
            "rule_type": self.rule_type,
            "message": self.message
        }
        if self.line_number is not None:
            report["line_number"] = self.line_number
        return report

    @classmethod
    def from_dict(cls, report_dict):
        return cls(**report_dict)

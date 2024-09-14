
# Static Code Analysis Tool

This tool provides a static code analysis for Python projects, focusing on security, maintainability, and best practices. It includes multiple built-in rules, such as cyclomatic complexity checks, function length enforcement, docstring validation, and more. The tool analyzes Python files and generates a detailed JSON report of potential issues.

## Features
- **Cyclomatic Complexity Analysis**: Detects functions with high cyclomatic complexity.
- **Function Length Enforcement**: Warns when a function exceeds a specified length.
- **Missing Docstring Detection**: Flags functions without a proper docstring.
- **Unused Variable Detection**: Identifies variables that are assigned but never used.
- **Variable Naming Convention Enforcement**: Ensures variables follow snake_case naming convention.
- **Security Vulnerability Detection**: Flags dangerous use of functions like `eval`, `exec`, and potential SQL injection patterns.

## Getting Started

### Prerequisites
- **Python 3.x**: The tool is built using Python and requires version 3 or above.
- Install the required Python packages by running:
  ```bash
  pip install -r requirements.txt
  ```

### Project Structure
```
static_code_analysis_tool/
│
├── main.py                         # Main entry point for running the analysis
├── parsers/                        # AST parsers for Python files
│   └── python_parser.py
├── reports/                        # Report generator logic
│   ├── report.py                   # Defines the structure of the report
│   └── report_generator.py         # Generates JSON reports
├── rule_engine/                    # All the rules for static analysis
│   ├── cyclomatic_complexity_rule.py
│   ├── function_length_rule.py
│   ├── missing_docstring_rule.py
│   ├── rule_executor.py            # Handles execution of rules
│   ├── rule_manager.py             # Manages and applies all rules
│   ├── security_vulnerability_rule.py
│   ├── unused_variable_rule.py
│   └── variable_naming_rule.py
├── tests/                          # Python test files for running static analysis
│   └── integrated_test_1_rule.py
│   └── test_code_sample1_rule.py
└── requirements.txt                # Required Python packages
```

### Usage

1. **Add Python files to be analyzed**:
   Place the `.py` files you want to analyze inside the `tests/` directory.

2. **Run the analysis**:
   Execute the `main.py` script to analyze all the Python files in the `tests/` folder.
   ```bash
   python main.py
   ```

3. **Review the generated report**:
   The analysis will generate a `report.json` file, which contains the results of the static analysis, including any warnings or issues found in the Python code.

### Example Report (`report.json`):
```json
[
    {
        "file_name": "test_cyclomatic.py",
        "rule_type": "cyclomatic_complexity",
        "message": "Function 'complex_function' has high cyclomatic complexity (7).",
        "line_number": 1
    },
    {
        "file_name": "test_docstring.py",
        "rule_type": "missing_docstring",
        "message": "Function 'my_function' is missing a docstring.",
        "line_number": 3
    }
]
```

### Adding New Rules
To add new rules:
1. Create a new Python file in the `rule_engine/` directory following the existing pattern.
2. Implement the `apply()` method to process the AST and generate warnings if needed.
3. Make sure to add the new rule to the `DynamicRuleManager` so it can be applied during the analysis.

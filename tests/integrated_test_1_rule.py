# tests/integrated_test.py

# Cyclomatic Complexity Test Case
def complex_function(a, b, c):
    if a > b:
        while b < c:
            b += 1
            if b % 2 == 0:
                try:
                    x = 1 / b
                except ZeroDivisionError:
                    x = 0
    elif a == b and b > c:
        for i in range(c):
            print(i)
    else:
        if a or c:
            b = a + c
    return b


# Missing Docstring Test Case
def function_without_docstring():
    print("This function lacks a docstring.")


def another_function_without_docstring():
    print("Another missing docstring.")


# Function Length Test Case
def long_function():
    # A function with many lines
    x = 1
    y = 2
    z = 3
    a = 4
    b = 5
    c = 6
    d = 7
    e = 8
    f = 9
    g = 10
    h = 11
    print(x, y, z, a, b, c, d, e, f, g, h)


# Unused Variables Test Case
def unused_variables_example():
    x = 10
    y = 20
    z = 30  # Unused variable 'z'
    return x + y


# Variable Naming Convention Test Case
def test_variable_naming():
    myVariable = 10  # Not following snake_case
    anotherVar = 20  # Not following snake_case
    _valid_var = 30  # Correct
    MY_CONSTANT = 40  # Also valid for constants
    return myVariable + anotherVar + _valid_var + MY_CONSTANT


# Security Vulnerabilities Test Case
def security_risk_example(user_input):
    eval(user_input)  # Use of eval is a potential security risk
    exec(user_input)  # Use of exec is a potential security risk

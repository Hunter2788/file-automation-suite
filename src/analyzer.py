import ast

def analyze_code(code: str):
    report = []
    issues = []

    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        return {
            "report": f"❌ Syntax Error detected: {e}",
            "issues": ["syntax_error"]
        }

    # Check functions
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if len(node.body) == 1:
                issues.append(f"Function '{node.name}' is very small (possible unnecessary function).")

        if isinstance(node, ast.For):
            report.append("Loop detected - check if list comprehension is possible.")

        if isinstance(node, ast.While):
            report.append("While loop detected - ensure termination condition is safe.")

    if not issues:
        report.append("No critical structural issues detected.")

    return {
        "report": "\n".join(report + issues),
        "issues": issues
    }

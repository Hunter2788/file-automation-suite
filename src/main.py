from analyzer import analyze_code
from refactor import improve_code

def main():
    print("\n=== PYCODE IMPROVER TOOL ===\n")

    print("Paste your Python code below (end with an empty line):\n")

    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    code = "\n".join(lines)

    print("\n--- ANALYZING CODE ---\n")
    analysis = analyze_code(code)

    print(analysis["report"])

    print("\n--- IMPROVED CODE ---\n")
    improved = improve_code(code, analysis)

    print(improved)

if __name__ == "__main__":
    main()

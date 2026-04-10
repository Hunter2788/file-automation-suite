from rules import IMPROVEMENTS

def improve_code(code: str, analysis: dict):
    improved = []

    improved.append("# === IMPROVED CODE VERSION ===\n")

    improved.append("# Suggestions applied:")
    for rule in IMPROVEMENTS:
        improved.append(f"# - {rule}")

    improved.append("\n# NOTE: This tool provides heuristic improvements only.\n")

    # Basic formatting improvement simulation
    lines = code.split("\n")

    cleaned = []
    for line in lines:
        cleaned.append(line.rstrip())

    improved.append("\n".join(cleaned))

    return "\n".join(improved)

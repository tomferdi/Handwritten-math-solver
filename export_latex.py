def save_as_tex(latex_expression, output_path="output.tex"):
    """Save LaTeX expression to a .tex file."""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"\\documentclass{{article}}\n\\begin{{document}}\n{latex_expression}\n\\end{{document}}")
    return output_path

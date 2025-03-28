import sympy as sp
from sympy.plotting import plot

def generate_graph(latex_expression):
    """Generate a graph from a mathematical function if applicable."""
    try:
        x = sp.Symbol('x')
        expr = sp.sympify(latex_expression.replace("^", "**"))
        plot(expr, (x, -10, 10), title="Graph", ylabel="y", xlabel="x")
    except Exception as e:
        print(f"Graph generation failed: {e}")

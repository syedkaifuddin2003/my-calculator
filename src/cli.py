"""
Command Line Interface for Calculator
Example usage:
    python -m src.cli add 5 3
    python src/cli.py add 5 3   # also supported thanks to fallback import
"""

import sys
import click

# Try relative import (works when run as package: python -m src.cli).
# If that fails (running the file directly: python src/cli.py), fall back
# to an absolute import which will work because the script's directory is
# added to sys.path when executed directly.
try:
    from .calculator import add, subtract, multiply, divide, power, square_root
except ImportError:
    from calculator import add, subtract, multiply, divide, power, square_root
@click.command()
@click.argument("operation")
@click.argument("num1", type=float)
@click.argument("num2", type=float, required=False)
def calculate(operation, num1, num2=None):
    """Simple calculator CLI"""
    try:
        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
        elif operation == "power":
            result = power(num1, num2)
        elif operation == "square_root" or operation == "sqrt":
            result = square_root(num1)
        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)
        return result
    except Exception as e:
        click.echo(f"Error: {e}")
        sys.exit(1)

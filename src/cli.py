"""
Command Line Interface for Calculator
Example usage:
    python -m src.cli add 5 3
    python -m src.cli divide 5 3
    python -m src.cli sqrt 9
"""

import sys
import click
# 👇 Use relative import so pylint & pytest can resolve it correctly
from .calculator import add, subtract, multiply, divide, power, square_root


@click.command()
@click.argument("operation")
@click.argument("num1", type=float)
@click.argument("num2", type=float, required=False)
def calculate(operation, num1, num2=None):
    """Simple calculator CLI"""
    try:
        # Perform the selected operation
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
        elif operation == "sqrt":
            result = square_root(num1)
        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)

        # Format output:
        #   - integers → no decimals
        #   - floats → 2 decimal places (for divide etc.)
        if isinstance(result, float) and result.is_integer():
            click.echo(int(result))
        elif isinstance(result, float):
            click.echo(f"{result:.2f}")
        else:
            click.echo(str(result))

    except ValueError as e:
        click.echo(f"Error: {e}")
        sys.exit(1)
    except ZeroDivisionError:
        click.echo("Error: Division by zero")
        sys.exit(1)
    except Exception as e:
        click.echo(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    calculate()

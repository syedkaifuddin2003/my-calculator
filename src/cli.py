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
        # Validate arity for 2-arg operations
        if operation in ("add", "subtract", "multiply", "divide", "power") and num2 is None:
            click.echo(f"Error: operation '{operation}' requires two numeric arguments")
            sys.exit(1)

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

        # Format output
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

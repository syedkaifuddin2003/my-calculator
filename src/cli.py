import sys
import click

try:
    from .calculator import add, subtract, multiply, divide, power, square_root
except ImportError:
    from calculator import add, subtract, multiply, divide, power, square_root

@click.command()
@click.argument("operation")
@click.argument("num1", type=float)
@click.argument("num2", type=float, required=False)
def cli(operation, num1, num2=None):
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
        elif operation in ("square_root", "sqrt"):
            result = square_root(num1)
        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)
        # Format result: integer as int, float as 2 decimal places
        if isinstance(result, (float, int)) and float(result).is_integer():
            click.echo(str(int(result)))
        else:
            click.echo(f"{result:.2f}")
    except ValueError as e:
        click.echo(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        click.echo(f"Unexpected error: {e}")
        sys.exit(1)

# This line is required for `python -m src.cli ...` to work!
cli = cli

if __name__ == "__main__":
    cli()

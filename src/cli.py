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
        click.echo(str(result))
    except Exception as e:
        click.echo(str(e))
        sys.exit(1)

if __name__ == "__main__":
    calculate()

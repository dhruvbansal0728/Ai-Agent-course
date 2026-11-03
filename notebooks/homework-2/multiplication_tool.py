from agents import function_tool

@function_tool
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers and return the result."""
    return a * b
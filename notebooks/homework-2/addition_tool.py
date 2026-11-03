from agents import function_tool

@function_tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers and return their sum."""
    return a + b
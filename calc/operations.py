"""Basic math operations."""

def add(a, b):
    """Add a and b."""

    return a + b

def sub(a, b):
    """Substract b from a."""

    return a - b

def mult(a, b):
    """Multiply a and b."""

    return a * b

def div(a, b):
    """Divide a by b."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
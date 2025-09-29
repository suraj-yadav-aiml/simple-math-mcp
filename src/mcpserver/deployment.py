from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mathematical-tools")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together.

    Args:
        a (int): The first number to add.
        b (int): The second number to add.

    Returns:
        int: The sum of a and b.

    Examples:
        >>> add(5, 3)
        8
        >>> add(-2, 7)
        5
    """
    return a + b


@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract the second number from the first number.

    Args:
        a (int): The number to subtract from (minuend).
        b (int): The number to subtract (subtrahend).

    Returns:
        int: The difference of a minus b.

    Examples:
        >>> subtract(10, 3)
        7
        >>> subtract(5, 8)
        -3
    """
    return a - b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers together.

    Args:
        a (int): The first number to multiply.
        b (int): The second number to multiply.

    Returns:
        int: The product of a and b.

    Examples:
        >>> multiply(4, 5)
        20
        >>> multiply(-3, 6)
        -18
    """
    return a * b


@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide the first number by the second number.

    Args:
        a (float): The dividend (number to be divided).
        b (float): The divisor (number to divide by).

    Returns:
        float: The quotient of a divided by b.

    Raises:
        ValueError: If b is zero (division by zero).

    Examples:
        >>> divide(10.0, 2.0)
        5.0
        >>> divide(7.5, 3.0)
        2.5
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


@mcp.tool()
def power(base: float, exponent: float) -> float:
    """Calculate base raised to the power of exponent.

    Args:
        base (float): The base number.
        exponent (float): The exponent to raise the base to.

    Returns:
        float: The result of base raised to the power of exponent.

    Examples:
        >>> power(2.0, 3.0)
        8.0
        >>> power(5.0, 0.5)
        2.23606797749979
    """
    return base ** exponent


@mcp.tool()
def square_root(n: float) -> float:
    """Calculate the square root of a number.

    Args:
        n (float): The number to calculate the square root of.

    Returns:
        float: The square root of n.

    Raises:
        ValueError: If n is negative.

    Examples:
        >>> square_root(16.0)
        4.0
        >>> square_root(2.0)
        1.4142135623730951
    """
    if n < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return n ** 0.5


@mcp.tool()
def factorial(n: int) -> int:
    """Calculate the factorial of a non-negative integer.

    The factorial of n (written as n!) is the product of all positive integers
    less than or equal to n. By definition, 0! = 1.

    Args:
        n (int): A non-negative integer to calculate the factorial of.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is negative.

    Examples:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
        >>> factorial(3)
        6
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


@mcp.tool()
def gcd(a: int, b: int) -> int:
    """Calculate the greatest common divisor of two integers.

    Uses the Euclidean algorithm to find the largest positive integer
    that divides both numbers without a remainder.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.

    Examples:
        >>> gcd(12, 8)
        4
        >>> gcd(15, 25)
        5
        >>> gcd(17, 13)
        1
    """
    while b:
        a, b = b, a % b
    return abs(a)


@mcp.tool()
def lcm(a: int, b: int) -> int:
    """Calculate the least common multiple of two integers.

    The least common multiple is the smallest positive integer that is
    divisible by both a and b.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The least common multiple of a and b. Returns 0 if either a or b is 0.

    Examples:
        >>> lcm(12, 8)
        24
        >>> lcm(15, 25)
        75
        >>> lcm(7, 3)
        21
    """
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


@mcp.tool()
def is_prime(n: int) -> bool:
    """Check if a number is prime.

    A prime number is a natural number greater than 1 that has no positive
    divisors other than 1 and itself.

    Args:
        n (int): The integer to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.

    Examples:
        >>> is_prime(7)
        True
        >>> is_prime(10)
        False
        >>> is_prime(2)
        True
        >>> is_prime(1)
        False
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
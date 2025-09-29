# Simple Math MCP Server

A Model Context Protocol (MCP) server that provides essential mathematical operations as tools. This server exposes a comprehensive set of mathematical functions that can be used by MCP-compatible clients like Claude Desktop.

## Features

- **Basic Arithmetic**: Addition, subtraction, multiplication, and division
- **Advanced Operations**: Power calculation and square root
- **Number Theory**: Factorial, GCD (Greatest Common Divisor), and LCM (Least Common Multiple)
- **Prime Testing**: Check if a number is prime
- **Error Handling**: Proper validation and error messages for invalid inputs
- **Type Safety**: Full type annotations for all functions

## Available Tools

### Basic Arithmetic
- `add(a, b)` - Add two numbers
- `subtract(a, b)` - Subtract second number from first
- `multiply(a, b)` - Multiply two numbers
- `divide(a, b)` - Divide first number by second (with zero-division protection)

### Advanced Math
- `power(base, exponent)` - Calculate base raised to exponent
- `square_root(n)` - Calculate square root (with negative number protection)

### Number Theory
- `factorial(n)` - Calculate factorial of non-negative integer
- `gcd(a, b)` - Find greatest common divisor using Euclidean algorithm
- `lcm(a, b)` - Find least common multiple
- `is_prime(n)` - Check if a number is prime

## Installation

Add the following configuration to your MCP client (e.g., Claude Desktop):

```json
{
  "mcpServers": {
    "simple-math-mcp": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/suraj-yadav-aiml/simple-math-mcp.git",
        "mcp-server"
      ]
    }
  }
}
```

## Usage Examples

Once installed and configured, you can use the mathematical tools through your MCP client:

### Basic Calculations
- "Add 15 and 27" → Uses `add(15, 27)` → Returns `42`
- "What's 100 divided by 4?" → Uses `divide(100, 4)` → Returns `25.0`

### Advanced Operations
- "Calculate 2 to the power of 8" → Uses `power(2, 8)` → Returns `256.0`
- "Find the square root of 144" → Uses `square_root(144)` → Returns `12.0`

### Number Theory
- "What's the factorial of 5?" → Uses `factorial(5)` → Returns `120`
- "Find GCD of 48 and 18" → Uses `gcd(48, 18)` → Returns `6`
- "Is 17 a prime number?" → Uses `is_prime(17)` → Returns `True`

## Project Structure

```
simple-math-mcp/
├── src/
│   └── mcpserver/
│       ├── __init__.py
│       ├── __main__.py          # Entry point
│       └── deployment.py        # Main server implementation
├── pyproject.toml              # Project configuration
├── requirements.txt            # Dependencies
└── README.md                  # This file
```

## Development


### Key Components

- **deployment.py**: Contains all mathematical tool implementations using FastMCP
- **__main__.py**: Entry point that starts the MCP server
- **pyproject.toml**: Project metadata and build configuration

### Adding New Tools

To add a new mathematical function:

1. Add the function to `src/mcpserver/deployment.py`
2. Decorate it with `@mcp.tool()`
3. Include comprehensive docstring with Args, Returns, and Examples
4. Add proper error handling for edge cases

Example:
```python
@mcp.tool()
def new_function(param: int) -> int:
    """Brief description of the function.

    Args:
        param (int): Description of parameter.

    Returns:
        int: Description of return value.

    Examples:
        >>> new_function(5)
        10
    """
    return param * 2
```


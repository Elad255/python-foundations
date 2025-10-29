
from typing import Union, Callable

Number=Union[int,float]


def add(a: Number, b: Number)->float:
    return float(a)+float(b)


def sub(a: Number, b: Number) -> float:
    return float(a) - float(b)


def mul(a: Number, b: Number) -> float:
    return float(a) * float(b)


def div(a: Number, b: Number) -> float:
    b = float(b)
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a) / b


OPS: dict[str, Callable[[Number, Number], float]] = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}



def calculate(expr: str) -> float:
    """
    Evaluate a simple expression with a single binary operator: 'a op b'.
    Examples: '3 + 4', '10/2', '7 * 6'
    """
    tokens = expr.replace(" ", "")
    for op in OPS:
        if op in tokens:
            left, right = tokens.split(op, 1)
            return OPS[op](float(left), float(right))
    # if we didn't return inside the loop, no supported operator was found
    raise ValueError("Expression must be like 'a+b', 'a-b', 'a*b', or 'a/b'")

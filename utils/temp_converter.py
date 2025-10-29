
from typing import Union

Number = Union[int,float]


def c_to_f(celsius: Number) -> float:
    """Convert Celsius to Fahrenheit."""
    try:
      c=float(celsius)
    except (TypeError,ValueError):
      raise ValueError("celsius must be a number")
    
    return (c * 9 / 5) + 32

    



def f_to_c(fahrenheit: Number) -> float:
    """Convert Fahrenheit to Celsius."""

    try:
        f = float(fahrenheit)
    except (TypeError, ValueError):
        raise ValueError("fahrenheit must be a number")

    return (f - 32) * 5 / 9



if __name__ == "__main__":  # pragma: no cover
    # simple CLI demo

    
    mode = input("Enter mode [c2f|f2c]: ").strip().lower()
    try:
        value=float(input("enter value:").strip())
        if mode=="c2f":
            print(f"{value}°C -> {c_to_f(value):.2f}°F")
        elif mode=="f2c":
            print(f"{value}°F -> {f_to_c(value):.2f}°C")
        else:
            print("Unknown mode. Use c2f or f2c.")
    except ValueError:
        print("Please enter a valid numeric value.")

           
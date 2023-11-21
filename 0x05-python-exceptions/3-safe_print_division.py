#!/usr/bin/python3

def safe_print_division(a, b):
    """
    a function that divides 2 integers and prints the result.

    Args:
    a: first integer.
    b: second integer.

    Returnes:
    the value of the division.
    otherwise: None.
    """
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)

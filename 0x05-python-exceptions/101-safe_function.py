#!/usr/bin/python3

from __future__ import print_function
import sys


def safe_function(fct, *args):
    """
    a function that executes a function safely.
    Args:
    fct: pointer to a function.
    *args: ...
    Returns:
    he result of the function.
    Otherwise, returns None if something happens during the function
    """
    try:
        result = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    else:
        return result

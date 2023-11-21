#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
     a function that prints the first x elements of a list and only integers.

     Args:
     my_list: The list of elements that contains any type.
     x: the number of elements to access in my_list.

     Returns:
      the real number of integers printed.
    """
    num = 0
    for n in range(0, x):
        try:
            print("{:d}".format(my_list[n]), end="")
            num += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (num)

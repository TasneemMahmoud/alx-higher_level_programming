#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """A function that Prints x elememts of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list.

    Returns:
        The real number of elements printed.
    """
    num = 0
    for n in range(x):
        try:
            print("{}".format(my_list[n]), end="")
            num += 1
        except IndexError:
            break
    print("")
    return (num)

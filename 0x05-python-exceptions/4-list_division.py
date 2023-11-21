#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    a function that divides element by element 2 lists.

    Args:
    my_list_1: first element.
    my_list_2: second element.
    list_length: The length of list.

    Returns:
    a new list (length = list_length) with all divisions.
    """
    list = []
    for n in range(0, list_length):
        try:
            res = my_list_1[n] / my_list_2[n]
        except TypeError:
            print("wrong type")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            list.append(res)
    return (list)

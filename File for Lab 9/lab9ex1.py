def first_last6(list1: list) -> bool:
    """Return True if either/both first and last element are assigned a value of 6
    >>> first_last6(test_list1)
    False
    >>> first_last6(test_list2)
    True
    >>> first_last6(test_list3)
    True
    """
    if list1[0] or list1[5] == 6:
        return True
    else:
        return False


test_list1 = [0, 1, 2, 3, 4, 5]
test_list2 = [6, 1, 2, 3, 4, 9]
test_list3 = [6, 1, 2, 3, 4, 6]

print(first_last6(test_list1))
print(first_last6(test_list2))
print(first_last6(test_list3))
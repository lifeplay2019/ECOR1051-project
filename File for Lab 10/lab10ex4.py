from typing import List


def centered_average(lst: List[int]) -> float:
    """Returns a centered average, an average that excludes the largest and
    smallest number in a list, of a user-input list.

    >>> centered_average([-145, 2, 2, 145])
    2
    >>> centered_average([1, 3, 8, 2, 25])
    3
    """
    avg = 0
    count = -1
    for i in lst:
        count += 1
        avg += lst[count]
        # print(i)
    avg -= max(lst)
    avg -= min(lst)
    avg /= (len(lst) - 2)
    return avg


print(centered_average([1, 1, 3, 6, 10, 15, 7]))
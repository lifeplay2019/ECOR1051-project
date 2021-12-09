def big_diff(list_one: list) -> float:
    """
    Returns the difference between the biggest and smallest items in a list.

    >>>big_diff([])
    List can not be empty
    >>>big_diff([1,4,7,2,6])
    6
    >>>big_diff([1,4,0,2,6])
    6
    >>>big_diff([1,2,4,5,6])
    5
    >>>big_diff([10, 3, 5, 6])
    7
    """
    if len(list_one) == 0:
        print('List can not be empty')
    else:
        min_num = max_num = list_one[0]
        for i in list_one:
            if i < min_num:
                min_num = i

            elif i > max_num:
                max_num = i

        print(max_num - min_num)
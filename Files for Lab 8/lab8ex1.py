def baker_party(number_of_parties:int, weekend:bool)->bool:
    """return the value of both number of parties which is an int, and the value 
    weekend which is bool (measuring in weekends or weekdays) and final get the 
    value which is a bool into True of False.
    >>>baker_party(40, False)
    False
    >>>baker_party(150, False)
    False
    >>>baker_party(60, True)
    false
    """
    if number_of_parties >= 40 and number_of_parties <= 60 and not weekend:
        return baker_party ==True
    if number_of_parties <= 40 and weekends:
        return baker_party ==True
    else:
        return baker_party ==False

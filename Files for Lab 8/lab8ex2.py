def squirrel_play(temperature : int, winter : bool) -> bool:
    """return the temperature with the int and the winter is bool which is not 
    yes. The variable is temperature and the winter.
    
    >>>squirrel_play(70, False)
    False
    >>>squirrel_play(95, False)
    False
    >>>squirrel_play(95, True)
    False
    """
    if  winter and (temperature >= 60 and temperature < 90) :
        return squirrel_play==True
    elif (not winter) and(temperature >= 60 and temperature <= 100) :
        return squirrel_play==True
    else:
        return False

 
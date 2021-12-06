def same_first_last(list1: list) -> bool:
     """The function returns True if the list is
     not empty and if the first and last elements are equal. Otherwise, 
     the function returns False
    
    
    >>>same_first_last([1,2,3,1])
    True
    >>>same_first_last([1,2,3,4])
    False
    

    """
     for i in list1:
       
          if list1[0] == list1[-1]:
               return True
   
          if list1[i] == []:
               return True
          else:
               return False
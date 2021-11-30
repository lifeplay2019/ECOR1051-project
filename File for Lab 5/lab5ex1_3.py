#Exercises 1
import math
def area_of_disk(radius: float)-> float:
    """ Return the area of the disk of the radius, which get the result of the area
    along with the non-negative radius. The dimensions of the area_of_disk in the frame
    is radius.
    
    Preconditions: radius > 0
    
    >>>area_of_disk(3)
    28.274333882308138
    >>>area_of_disk(4)
    50.26548245743669
    >>>area_of_disk(5)
    78.53981633974483
    
     
    
    """
    return math.pi * radius ** 2
area = area_of_disk(3)
area = area_of_disk(4)
area = area_of_disk(5)


#Exercise 2
import math
def calculateDistance(x1,y1,x2,y2):
    """to deternmine the distance between x1 y1 and x2 y2
    by checking http://mathworld.wolfram.com/PythagoreanTheorem.html notice that 
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     
     The dimensions of the calculateDistance in the frame are x1, x2, y1, y2
     
     >>>calculateDistance(1, 1, 2, 2)
     1.414213562
     >>>calculateDistance(2, 2, 3, 3)
     1.414213562
     >>>calculateDistance(3, 3, 4, 4)
     1.414213562
     and get the return to the distance of two point
    
    
    """
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
    return dist
disk =  calculateDistance(1,1,2,2)
disk =  calculateDistance(2,2,3,3)
disk =  calculateDistance(3,3,4,4)

#Exercise 3
import math
def distance(x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        dsquared = dx**2 + dy**2
        result = dsquared**0.5
        return result

def area(radius):
    """Return the area of a radius frame with dimensions radius. 
    The dimensions of the area in the frame
    are radius.
    
    Preconditions: radius > 0
    
    """    
    b = math.pi*radius**2
    return b

   
def area_of_circle(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    """First get the result of the distance the radius
    by using the Exercise 2
    The second of the def caluate the area of the radius
    by  = math.pi*radius**2
    
    Preconditions: radius > 0
    
    
    """
    return result

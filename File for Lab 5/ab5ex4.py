
import math

def height(length: float, angle: float):

    '''

    Function height returns the height of the point

    to wall where ladder touches the wall.

    length is in meter and value of angle is in degree and

    must be in range 0<angle<90

    '''

    return length*math.sin(math.radians(angle))
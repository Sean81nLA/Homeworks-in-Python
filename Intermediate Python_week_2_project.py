
def count_uppercase_letters(my_string):
    '''Return number of upper case letters in string.

    Parameters
    ----------
    my_string: str
         the string that processed for number of uppercase characters

    Returns
    ----------
    counter: int
         the number of uppercase characters in the input string
    '''

    counter = sum(1 for char in my_string if char.isupper())
    return counter

def interleave_lists(list_1,list_2):
    '''Interleave two lists to create a third list.

    Parameters
    ----------
    list_1 : list
         first list to be interleaved

    list_2 : list
         second list to be interleaved

    Returns
    ----------
    list_3: list
    '''
    list_3 = []
    for i in range(len(list_1)):
        list_3.append(list_1[i])
        list_3.append(list_2[i])
    return list_3

def cylinder_stats(radius, height):
    '''Calculate surface area and vlume of a solid right circular cylinder.

    Parameters
    ----------
    radius: int, float
         the radius of the cylinder being analyzed
    height: int, float
         the height of the cylinder being analyzed

    Returns
    ----------
    surface_area: float
         the surface area of the cylinder being analyzed
    volume: float
         the volume of the cylinder being analyzed
    '''
    import math
    surface_area = 2 * math.pi * radius * ( height + radius)
    volume = math.pi * (radius ** 2) * height
    return surface_area, volume

'''
Count_uppercase_letters(my_string).

Parameters
----------------
my_string: string

Returns
----------------
Count of capital letters in a string

'''

def count_uppercase_letters(my_string):
    count = 0
    for letter in my_string:
        if (letter.istitle()):
           count = count+1
    return (count)

result = count_uppercase_letters ('The Quick Brown Fox')
print(result)

'''
interleave_lists(list_1, list_2).

Parameters
----------------
List_1: letter or number,

List_2: letter or number,

Returns
----------------
This function will two take arguments, both lists. It will interleave the items in the list
'''

def interleave_lists(list_1, list_2):
    res = [i for j in map(None, list_1, list_2)   
                       for i in j if i is not None] 
    return (str(res))

list_1=[1,2,3,4]
list_2=['a','b','c','d']
result = interleave_lists(list_1, list_2)
print(result)

'''
cylinder_stats(radius, height).

Parameters
----------------
radius of a cylinder: float or Int

height of a cylinder: float or Int

Returns
----------------
area: float or Int
    the area of the cylinder
Volume: float or int
    the volume of the cylinder

'''
def cylinder_stats(radius, height):
    import math
    Surface_Area = 2*math.pi*radius*(height + radius)
    Volume = math.pi*(radius**2)*height
    return(Surface_Area, Volume)

result = cylinder_stats (5,10)
print(result)

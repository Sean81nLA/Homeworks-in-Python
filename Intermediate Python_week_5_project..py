import logging


# Problem 1 Possible Solution
logging.basicConfig(filename='week5.log', level=logging.DEBUG)
def mylogging(func):
        """create a function that executes func and creates a log entry with the function name and arguments"""
        def wrapper(*args, **kwargs):
            '''log the name of func and its arguments and then execute func
            '''
            logging.debug("The {} function ran with the following arguments:'-POSITIONAL-' {} '-KEYWORD-' {}".format(func.__name__, args, kwargs))
            result = func(*args,**kwargs)
            return result
        return wrapper
            
# Problem 2 Possible Solution
class Person:
    '''A class to model a person 
    
    Parameters
    ----------
    name : str
        person's name
        
    weight : int, float
        persons's weight in kilograms
       
    height : int, float
        persons's height in meters
        
    '''
    def __init__(self, name, height, weight):
        '''Initialize the Person object'''
        self.name = name
        self.height = height
        self.weight = weight
    @property
    def bmi(self):
        '''Calculate BMI from height and weight'''
        return (self.weight / self.height ** 2)


# Problem 3 Possible Solution
class LinearModel:
    '''LinearModel Class to make predictions according to the model y=mx+b
    
    Parameters
    ----------
    m : float, int
        the slope constant
    
    b : float, int
        the intercept constant
    '''
    
    def __init__(self,m,b):
        '''initialize object'''
        self.m = m
        self.b = b
    
    def predict(self, x):
        '''predict value of y in y = mx + b'''
        return (self.m * x + self.b)


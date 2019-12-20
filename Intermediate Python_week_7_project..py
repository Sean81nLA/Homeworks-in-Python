import numpy as np

def list_is_in(list1, list2):
    '''Return a list of the same length as list 1, but with a entry of True
    or False depending on if the item at that index in list1 is in list2
    '''
    set2 = set(list2)
    res = []
    for item in list1:
        if item in set2:
            res.append('True')
        else:
            res.append('False')
    return res

def mean_normalize(nparray):
    '''Normalize array with respect each columns by subtracting the mean
    of each column and dividing by the standard deviation of each column
    '''
    return (nparray - nparray.mean(axis=0))/nparray.std(axis=0)

class temperature_model():
    '''Temperature Data Model
    
    Parameters
    ----------
    filepath : str
        The path to a csv of temperature data. Each row is expected to be a
        separate weather station and each column an hourly temperature reading
    '''
    def __init__(self,filepath):
        self.filepath = filepath
        self.my_array = np.loadtxt(filepath, delimiter=',')

    def mean_normalize(self):
        '''Return the tempearture data, normalized wrt station. Normalize
        by subtracting the mean of each station and then dividing by the standard
        deviation of each station.
        '''
        mean = self.my_array.mean(axis=1).reshape(-1,1)
        std = self.my_array.std(axis=1).reshape(-1,1)
        return (self.my_array - mean)/std

from datetime import datetime

# Problem 1 Possible Solution
class Vehicle:
    '''A class representing a generic vehicle'''
    def __init__(self, weight, horsepower):
        self.weight = weight
        self.horsepower = horsepower
    def drive(self):
        '''A method representing the drive functionality '''
        print('The vehicle is driving')
    def stop(stop):
        '''A method representing the stop functionality '''
        print('The vehicle has stopped.')

class Car(Vehicle):
    '''A class representing a car '''
    def __init__(self, weight, horsepower):
        self.wheels = 4
        super().__init__(weight, horsepower)

class Motorcycle(Vehicle):
    '''A class representing a motorcycle '''
    def __init__(self, weight, horsepower):
        self.wheels = 2
        super().__init__(weight, horsepower)

    def wheelie(self):
        '''A method representing the wheelie functionality '''
        print('I popped a wheelie.')

class Bus(Vehicle):
    '''A class representing a motorcycle '''
    def __init__(self, weight, horsepower):
        self.wheels = 6
        super().__init__(weight, horsepower)

    def dump(self):
        '''A method representing the 'dump' functionality '''
        print('I am dumping the load.')

# Problem 2 Possible Solution
class NumericList(list):
    '''Modified list class that includes a method, "product" that returns product of numbers in list'''
    def product(self):
        '''Method that calculates the product of numbers in list'''
        result = 1
        for _ in self:
             result = result * _
        return result

# Problem 3 Possible Solution
class Customer:
    '''
    A class to model customers

    Parameters
    ----------
    customer_number : int, str
        the numerical customer id

    customer_info_filepath : str
        the filepath to the customer info file

    purchases_filepath : str
        the filepath to the purchases file

    '''
    def __init__(self, customer_number, customer_info_filepath,
                 purchases_filepath):
        self.customer_number = str(customer_number)
        self.customer_info_filepath = customer_info_filepath
        self.purchases_filepath = purchases_filepath
        self.purchases = {}

    def _load_customer_info(self):
        '''Load the data from the customer info file for this customer'''
        with open(self.customer_info_filepath, 'r') as read_file:
            for line in read_file:
                line_splits = line.strip().split(',')
                if line_splits[0] == self.customer_number:
                    self.name = line_splits[1]
                    self.age = line_splits[2]
                    self.state = line_splits[3]
                    break

    def _load_purchases(self):
        '''Load the purchases data from the purchases file, for this customer
        '''
        with open(self.purchases_filepath, 'r') as read_file:
            for line in read_file:
                line_splits = line.strip().split(',')
                if line_splits[0] == self.customer_number:
                    purchase_date = datetime.strptime(line_splits[1],
                                                      "%Y-%m-%d %H:%M:%S")
                    self.purchases[purchase_date] = line_splits[2]

    def load_data(self):
        '''Load all the customers data'''
        self._load_customer_info()
        self._load_purchases()

    def get_last_purchase(self):
        '''return the most recent purchase made by the customer'''
        return self.purchases[max(self.purchases.keys())]

    def get_first_purchase(self):
        '''return the most recent purchase made by the customer'''
        return self.purchases[min(self.purchases.keys())]

    def get_num_purchases(self):
        '''return the total number of purchases made by the customer'''
        return len(self.purchases)

    def get_sum_of_purchases(self):
        '''return the total purchase amount made by the customer'''
        sum = 0
        for value in self.purchases.values():
            sum = sum + float(value)
        return sum
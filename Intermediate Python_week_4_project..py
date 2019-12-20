# Problem 1 Possible Solution

def raise_to_power(n):
   """Returns a function that raises any number to the nth power."""

   def x_to_the_n(x):
      """Return x to the nth power."""
      result = x**n
      return result

   return x_to_the_n


# Problem 2 Possible Solution

def file_writer(filepath):
   """Return a function that will write to the filepath"""

   def write_s_to_filepath(s):
      """Append the string, s, to a file"""

      with open(filepath, 'a') as f:
         f.write(s) 

   return write_s_to_filepath


# Problem 3 Possible Solution

def word_n_of_each_line(n):
   """Return a function that will return the nth word of each line of any file passed to it."""

   def nth_word_generator(file):
      with open(file, 'r') as f:
        for line in f:
            if len(line.strip().split()) < n:
              yield "None"
            else:
               yield line.strip().split()[n - 1]

   return nth_word_generator


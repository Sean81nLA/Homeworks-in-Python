# Problem 1 Possible Solution
def all_the_kwargs(**kwargs):
    """Return the number of keyword arguments that are passed

    Parameters
    ----------
    **kwargs:
         any keyword arguments

    Returns
    ----------
    kwargs_counter: int
         the number of kwargs passed to the function
    """
    kwargs_counter = len(kwargs)
    return kwargs_counter

# Problem 2 Possible Solution
def almost_fibonacci(N):
    """Generate the almost fibonacci series (each number is sum of previous 3 in sequence) starting at 0, 1 and 1

    Parameters
    ----------
    N: int
         number of values in sequence to be calculated

    Yields
    ----------
    i: int
         number in sequence
    """
    i_prev_2, i_prev_1, i = 0, 1, 1
    yield i_prev_2
    yield i_prev_1
    for _ in range(N-2):
        yield i
        i, i_prev_1, i_prev_2 = i + i_prev_1 + i_prev_2, i, i_prev_1

# Problem 3 Possible Solution
def first_word_of_each_line(filepath):
    """ select and yield first word of every line of a given text file

    Parameters
    ----------
    filepath: str
         path to text file to be processed

    Yields
    ----------
    word: str
         the first word on a given line of a text file
    """
    with open(filepath, 'r') as my_file:
        for line in my_file:
            line = line.strip()
            words = line.split()
            word = words[0]
            yield word
import random


def random_number(x, y):  # method for random integers
    rng = random.Random()
    number = rng.randint(x, y)
    return number


def n_random_numbers(x, y, n):
    '''
    return n random integers (as a list) between integers x and y
    '''
    random_numbers = random.sample(range(x, y+1), n)
    return random_numbers

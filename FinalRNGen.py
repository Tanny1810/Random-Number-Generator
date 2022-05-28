'''
I start with the random number generator
since we are working with computers, which are deterministic, we can only make a pseudo random number generator
the first thing I learned was how pseudo random number generators work
and then implemented my own in the following way:
'''
import matplotlib.pyplot as plt


def pseudo_rand_gen(low, high, size, seed):
    weight = 1337  # random number
    bias = 420  # also random number
    mod = (2**42)-1  # limiter on value generated (optimisation step)
    # generate a list of zeroes, which we fill with random numbers
    random_vals = [0]*size
    # using y=wx+b or mx+c, we can find a linear expression for a given seed
    x = (weight * seed + bias) % mod
    # we can then use this linear expression to find the first random number, scaled by mod
    random_vals[0] = x/mod
    for i in range(1, size):
        # start compunding the randomness by iteratively running the same linear function on our x value
        x = (weight * x + bias) % mod
        # fit our value to the range provided by low and high, and add it to the list
        random_vals[i] = low + (high - low) * x/mod
    return random_vals


'''
the issue at this point, was that I would always generate the same list of random numbers, given the same starting seed
so the next step was to find a random seed
since I was not allowed to use libraries, I could not access date time as my seed
code execution time was another alternative, which was possible in jupyter notebook, but not in a single .py file
so I looked into accessing the memory addresses of variables
using id, I could find the memory address of a variable
and the memory address of a variable is a unique number if and only if the variable is a list with some values inside
I will get into this after the code 
'''

ls = [69]  # completely pointless list, just to access a unique memory address each time the code is run
# we now get the seed from the memory address of the list
completely_random_seed = id(ls)

'''
since a list is a mutable, python assigns it different memory locations each time it is run
passing the seed into the pseudo_rand_gen function, will generate a different list of random numbers each time
'''

random_nums_list = pseudo_rand_gen(
    low=0, high=20, size=200000, seed=completely_random_seed)
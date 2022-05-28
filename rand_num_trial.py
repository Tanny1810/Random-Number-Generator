# write a code that generates a random number without using any libraries in python
import matplotlib.pyplot as plt

# Generates a list of zeros of size n

# generate a function to return a string


def zeros(n):
    return [0]*n


def pseudo_rand_gen(low, high, size, seed):
    mult = 16807
    mod = (2**31)-1
    U = zeros(size)
    x = (seed * mult+1) % mod
    U[0] = x/mod
    for i in range(1, size):
        x = (x * mult + 1) % mod
        U[i] = low + (high - low) * x/mod
    return U


# def call_me_twice(low, high, size, seed):

#     rand_sols = []
#     for i in range(50):
#         temp_sol = pseudo_rand_gen(low, high, size, seed)
#         rand_sols.append(temp_sol)

#     # pick randomly from rand_sols

#     return rand_sol

    # U1 = pseudo_rand_gen(low, high, size, seed)
    # seed = U1[int(seed % (size/high))]
    # U2 = pseudo_rand_gen(low, high, size, seed)
    # # U2 = pseudo_rand_gen(low, high, size, random_choose(U1))
    # return U2


# calling the random number generator function
# low and high is the range of the random numbers

ls = [69]  # completely pointless list, just to access a unique memory address each time the code is run
# we now get the seed from the memory address of the list
completely_random_seed = id(ls)
random_numbers = pseudo_rand_gen(
    low=-5, high=6, size=10000, seed=completely_random_seed)

# Graph plot
print(random_numbers)
plt.hist(random_numbers, bins=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlim(-6, 8)
plt.show()

# write a code that generates a random number without using any libraries in python
import matplotlib.pyplot as plt


def zeros(n):
    """
    Generates a list of zeros
    """
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


# calling the random number generator function
random_numbers = pseudo_rand_gen(
    low=-5, high=6, size=10000, seed=123456789)

# Graph plot
print(random_numbers)
plt.hist(random_numbers, bins=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlim(-6, 8)
plt.show()

# write a code that generates a random number without using any libraries in python
import matplotlib.pyplot as plt


def zeros(n):
    """
    Generates a list of zeros
    """
    return [0]*n


def float_to_int(x):
    """
    Converts a float to an integer
    """
    int_val = int(x*1000000)
    # print(int_val)
    return int_val

# print(float_to_int(0.345155513))


def negative_conv(x):
    """
    Selects a number to become negative or not
    """
    new_val = float_to_int(x)
    # print("MOD:", new_val % 10)
    if ((new_val % 10000) % 2 == 0):
        return -1*x
    else:
        return x


def rand_gen(size, seed):
    mult = 16807
    mod = (2**31)-1
    U = zeros(size)
    x = (seed * mult+1) % mod
    U[0] = x/mod
    for i in range(1, size):
        x = (x * mult + 1) % mod
        U[i] = negative_conv(x/mod)
    return U


def pseudo_uniform_rand_num(low, high, size, seed):
    summ = low + (high - low)
    return summ * rand_gen(size, seed)


# calling the random number generator function
random_numbers = pseudo_uniform_rand_num(
    low=-9, high=6, size=100, seed=1234567)

# Graph plot
print(random_numbers)
plt.hist(random_numbers, bins=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlim(-6, 8)
plt.show()

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


def sum_of_primes_in_list(l):
    sum = 0
    for item in l:
        if is_prime(item):
            sum += item
    return sum


# test
print(sum_of_primes_in_list([2, 3, 5, 4, 7, 9, 6, 13]))

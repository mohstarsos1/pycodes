def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


# test
print(is_prime(11))
print(is_prime(15))
print(is_prime(2))

import math


def check_prime_num(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):  # 2~ n의제곱근까지만 확인해주면 됨!
        if n % i == 0:
            return False

    return True

def euclidean_algorithm(a: int, b: int) -> int:
    '''
    This function deploys the euclidean algorithm to obtain the greatest
    common divisor of two numbers a and b.
    '''
    max_num = max(a,b)
    min_num = min(a,b)
    quotient = max_num // min_num
    remainder = max_num % min_num
    print(f"{max_num} = {min_num} * {quotient} + {remainder}")
    while remainder != 0:
        max_num = min_num
        min_num = remainder
        remainder = max_num % min_num
        print(f"{max_num} = {min_num} * {quotient} + {remainder}")
    return min_num

def euler_phi(n: int) -> int:
    '''
    This function calculates the Euler's totient function for a given integer n.
    It counts the integers up to n that are coprime with n.
    '''
    if n < 1:
        return 0
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result
def euclidean_algorithm(a: int, b: int) -> int:
    '''
    This function deploys the euclidean algorithm to obtain the greatest
    common divisor of two numbers a and b.
    '''
    max_num = max(a,b)
    min_num = min(a,b)
    remainder = max_num % min_num
    while remainder != 0:
        max_num = min_num
        min_num = remainder
        remainder = max_num % min_num
    return min_num
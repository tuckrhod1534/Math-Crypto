import math

def brute_discrete_log(base: int, result: int, modulus: int):
    for n in range(modulus - 1):
        if base**n % modulus == result:
            print(f"{base}^{n} == {base**n % modulus} (mod {modulus})")
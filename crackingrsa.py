def multiplicative_inverse(a, b):
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = a  # Remember original a/b to remove
    ob = b  # negative values from return results
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob  # If neg wrap modulo orignal b
    if ly < 0:
        ly += oa  # If neg wrap modulo orignal a
    return lx
def primefinder():
    result = []
    number = 2
    primesfound = 0
    while primesfound < 200:
        for i in range(2,number):
            if (number % i) == 0:
                break
        else:
            result.append(number)
            primesfound += 1
        number += 1
    return result
def factorfinder(primes, n):
    factors = []
    for p in primes:
        for q in primes:
            if p*q == n:
                factors = [p, q]
                break
    return factors
primes = primefinder()
for i in range(int(input())):
    p, q = input().split(" ")
    n, e = int(p), int(q)
    factors = factorfinder(primes, n)
    phi = (factors[0]-1)*(factors[1]-1)
    d = multiplicative_inverse(e, phi)
    print(d)
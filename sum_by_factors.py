from math import sqrt
from collections import defaultdict


def sum_for_list(lst):
    known_primes = {2: 0}
    for i in xrange(max(map(abs, lst))):
        if is_prime(i):
            known_primes[i] = 0

    #print 'known_primes for max({0}): {1}'.format(max(lst), sorted(known_primes))
    prime_factors = defaultdict(lambda: 0)
    for item in lst:
        for prime in known_primes:
            if item % prime == 0:
                prime_factors[prime] += item

    return [[key, prime_factors[key]] for key in sorted(prime_factors)]


def is_prime(num):

    if num <= 2 or (num % 2) == 0:
        if num == 2:
            return True
        else:
            return False

    for i in xrange(3, int(sqrt(num))+1, 2):
        if (num % i) == 0:
            return False
    return True


print sum_for_list([12, 15])
print sum_for_list([15, 30, -45])
print sum_for_list([107, 158, 204, 100, 118, 123, 126, 110, 116, 100]), 'should equal [[2, 1032], [3, 453], [5, 310], [7, 126], [11, 110], [17, 204], [29, 116], [41, 123], [59, 118], [79, 158], [107, 107]]'
print sum_for_list([-29804, -4209, -28265, -72769, -31744])
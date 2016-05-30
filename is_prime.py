def is_prime(num):
    if num <= 2 or (num % 2) == 0:
        if num == 2:
            return True
        else:
            return False

    for i in xrange(3, num / 2 + 1, 2):
        if (num % i) == 0:
            return False
    return True

print [(x, is_prime(x)) for x in xrange(17)]

def breakChocolate(n, m):

    if n <= 0 or m <= 0:
        return 0

    mbreaks = m-1
    nbreaks = m*(n-1)
    return mbreaks + nbreaks

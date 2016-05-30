import itertools


def is_merge(s, part1, part2):
    ''' Return False if combined length of parts is not equal to length
        of s or set of letters is parts is not the same as in s '''
    parts = part1+part2
    if not set(parts) == set(s) or len(s) != len(parts):
        return False

    for i, letter in enumerate(s):
        pairs = itertools.izip_longest(part1, part2)
        print list(pairs)
        next_pair = pairs.next()
        pair = next_pair

        if pair[0] == pair[1]:
            j = 0
            while next_pair[0] == next_pair[1]:
                j += 1
                next_pair = pairs.next()
            if letter in next_pair[1]:
                # Swap part1 and part2
                temp = part1
                part1 = part2
                part2 = temp

        if letter not in pair:
            print 'letter {0} not in parts {1}'.format(letter, pair)
            return False

        if letter == pair[0]:
            part1 = part1[1:]
        if letter == pair[1]:
            part2 = part2[1:]

    return False


print is_merge('codewars', 'code', 'wars')
print is_merge('Bananas from Bahamas', 'Bahas', 'Bananas from am')
print is_merge('Can we merge it? Yes, we can!', 'Can mer it?Y cn', 
               'wege es, wea!')
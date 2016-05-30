def goodVsEvil(good, evil):
    weight_good = [1, 2, 3, 3, 4, 10]
    weight_evil = [1, 2, 2, 2, 3, 5, 10]

    print good.split()
    print weight_good
    good_points = [a*b for a, b in zip(map(int, good.split(' ')), weight_good)]
    print(good_points)


goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1')
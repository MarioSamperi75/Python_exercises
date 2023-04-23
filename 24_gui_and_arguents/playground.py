def add(*args):
    tot = 0
    for arg in args:
        tot += arg
    return tot


print(add(2, 3, 4, 5, 6))

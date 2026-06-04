def sum_of(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(sum_of(1,2,3,4,5))
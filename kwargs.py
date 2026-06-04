def sum_of(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return sum

print(sum_of(a=1, b=2, c=3, d=4, e=5))
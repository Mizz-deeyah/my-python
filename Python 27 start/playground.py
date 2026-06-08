def add(*args):
    sum = sum = 0
    for n in args:
        sum += n
        return sum

        sum += n
print(add(3, 5, 6, 2,1, 7, 4, 3))


def calculate(**kwargs):
    print(kwargs)
calculate(add=3, multiply=5)
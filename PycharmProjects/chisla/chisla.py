
def is_simple(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


for i in range(2, 101):
    if is_simple(i):
        print('value {} is simple'.format(i))
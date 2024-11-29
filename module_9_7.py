def is_prime(func):
    def wrapper(*args, **kwargs):
        numbers = func(*args, **kwargs)
        k = False
        if numbers > 1:
            for i in range(2, numbers // 2 + 1):
                if numbers % i == 0:
                    k = True
            if not k:
                print('Простое')
            else:
                print('Составное')
            return numbers

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)

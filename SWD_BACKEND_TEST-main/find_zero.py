def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


def find_zero_at_last(n):
    count = 0
    while n % 10 == 0 and n != 0 :
        count += 1
        n //= 10
    return count


print(find_zero_at_last(factorial(120)))

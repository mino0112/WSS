def fibonacci_mod(n, m):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b) % m
    return a

def pisano_period(m):
    a, b = 0, 1
    period = [a]
    for _ in range(m * m):
        a, b = b, (a + b) % m
        period.append(a)
        # Check if the period restarts with 0, 1
        if a == 0 and b == 1:
            return period[:-1]
    return period

def count_zeros_in_pisano_period(n):
    period = pisano_period(n)
    zero_count = period.count(0)
    return zero_count

n = int(input())
zeros = count_zeros_in_pisano_period(n)
print(zeros)

# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45

    fib_table = [0, 1]

    for i in range(1, n + 1):
        if i <= 1:
            continue

        fib_table.append(fib_table[i - 1] + fib_table[i - 2])

    return fib_table[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))

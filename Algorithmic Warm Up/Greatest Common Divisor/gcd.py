# python3
import math


def gcd_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    for divisor in range(min(a, b), 0, -1):
        if a % divisor == 0 and b % divisor == 0:
            return divisor

    assert False


COUNTER = 0


def gcd(a, b):
    assert 0 <= a <= 2 * 10 ** 9 and 0 <= b <= 2 * 10 ** 9

    global COUNTER
    COUNTER = COUNTER + 1
    #print("iteration {}".format(COUNTER))
    if 0 == b:
        return a

    remainder = a % b

    return gcd(b, remainder)


if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(gcd(input_a, input_b))

    # O(log(ab))
    #print("BigO(log({}*{})) => {}".format(input_a, input_b, math.log10(input_a * input_b)))

"""
Hi, here's your problem today. This problem was recently asked by Apple:

Given a non-negative integer n, convert n to base 2 in string form. Do not use any built in base 2 conversion
functions like bin.


In the above example, 2^6 + 2^5 + 2^4 + 2^3 + 2^1 + 2^0 = 123.
"""

from collections import deque


def base_2(number: int) -> str:
    binary_value = deque()
    quotient = number

    while quotient > 0:
        binary_value.append(str(quotient % 2))
        quotient = quotient // 2

    binary_value.reverse()
    return ''.join(binary_value)


if __name__ == "__main__":
    print(base_2(number=123))
    print(base_2(492))
    # 1111011

 
"""Advent of Code - Problem 13"""

from typing import List, Tuple
import math



def read_data(filepath: str) -> Tuple[int, List[int]]:
    """Read bus departure time from first line and bus IDs from second."""
    with open(filepath, 'r') as infile:
        lines = [line.strip() for line in infile.readlines()]
    depart = int(lines[0])
    ids = [int(id_) if id_ != 'x' else None for id_ in lines[1].split(',')]
    return depart, ids


def calc_earliest_time_for_bus(depart: int, id_: int) -> int:
    """Calculate the earliest time after we can depart for bus of given id."""
    earliest_time = id_ - (depart % id_)
    return earliest_time


def find_earliest_bus_and_time(depart: int, ids: List[int]) -> Tuple[int, int]:
    """Find the earliest time at which a bus can depart."""
    earliest_time = None
    earliest_bus = None
    for id_ in ids:
        if id_:
            earliest_time_this_bus = calc_earliest_time_for_bus(depart, id_)
            if not earliest_time or earliest_time_this_bus < earliest_time:
                earliest_time = earliest_time_this_bus
                earliest_bus = id_

    return earliest_time, earliest_bus


def chinese_remainder(n: int, N: int, a: int) -> int:
    """Chinese Remainder Theorem - Algorithm."""
    result = 0
    for i, ni in enumerate(n):
        ai = a[i]
        bi = N // ni
        result += ai * bi * invmod(bi, ni)
    return result % N


def egcd(a: int, b: int) -> Tuple[int, int, int]:
    """Euclidean Greatest Common Divisor."""
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)


def invmod(a: int, m: int) -> int:
    """Inverse multiplicative modulo operator."""
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    return x % m


if __name__ == '__main__':
    DATA_FILEPATH = './Day13/day13.txt'

    depart, ids = read_data(DATA_FILEPATH)

    # Part A
    earliest_time, earliest_bus = find_earliest_bus_and_time(depart, ids)
    print('Part A - Find Earliest Time & Bus:', earliest_time, '&', earliest_bus)
    print('Part A - Answer:', earliest_time * earliest_bus)

    # Part B - Use Chinese Remainder Theorem
    n = []
    a = []
    for id_index, id_ in enumerate(ids):
        if id_:
            n.append(id_)
            a.append(-id_index)

    N = math.prod(n)
    ans = chinese_remainder(n, N, a)
    print('Part B:', ans)


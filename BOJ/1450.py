import sys 
from bisect import bisect_right
from itertools import combinations

def get_all_possible_case(weights, c):
    possible = []
    for i in range(1, len(weights) + 1):
        for comb in combinations(weights, i):
            curr_sum = sum(comb)
            if curr_sum <= c:
                possible.append(curr_sum)
    return possible


def count_possible_nums(weights, n, c):
    mid = n // 2
    
    weights_left, weights_right = weights[:mid], weights[mid:]

    possible_left = get_all_possible_case(weights_left, c)
    possible_right = sorted(get_all_possible_case(weights_right, c))

    count = 1 + len(possible_left) + len(possible_right)
    for case in possible_left:
        if case >= c:
            continue
        count += bisect_right(possible_right, c - case)
    return count

if __name__ == '__main__':
    input = sys.stdin.readline
    n, c = map(int, input().split())
    weights = list(map(int, input().split()))
    print(count_possible_nums(weights, n, c))
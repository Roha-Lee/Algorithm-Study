import sys 
from bisect import bisect_right, bisect_left

def generate_all_possible_partial_sum(n, A):
    prefix_A = [0] * (n+1)
    
    part_sum = 0
    for i in range(1, n+1):
        part_sum += A[i-1]
        prefix_A[i] = part_sum
    
    part_sum_A = []
    for i in range(n):
        for j in range(i+1, n+1):
            part_sum_A.append(prefix_A[j] - prefix_A[i])
    
    return part_sum_A


def count_sum_of_two_partial_sum(t, n, m, A, B):
    part_sum_A = generate_all_possible_partial_sum(n, A)
    part_sum_B = generate_all_possible_partial_sum(m, B)
    part_sum_A = sorted(part_sum_A)
    part_sum_B = sorted(part_sum_B)
    count = 0 
    for part_sum in part_sum_A:
        remain = t - part_sum
        count += bisect_right(part_sum_B, remain) - bisect_left(part_sum_B, remain)
    return count


if __name__ == '__main__':
    input = sys.stdin.readline
    t = int(input())
    n = int(input())
    A = list(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))
    print(count_sum_of_two_partial_sum(t, n, m, A, B))

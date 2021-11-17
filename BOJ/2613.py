import sys
from typing import final 
def is_valid_upperbound(bids, num_groups, upperbound, partition_elements):
    if upperbound < max(bids):
        return False
    temp_sum = 0
    group = 1
    count_bid = 0
    for bid in bids:
        if temp_sum + bid <= upperbound:
            temp_sum += bid
            count_bid += 1
        else:
            group += 1
            partition_elements.append((count_bid, temp_sum))
            count_bid = 1
            temp_sum = bid
        
    if group <= num_groups:
        partition_elements.append((count_bid, temp_sum))
        return True
    return False


def find_supremum(m, bids):
    left, right = min(bids), sum(bids)
    supremum = 0
    best_partition = []
    while left <= right: 
        mid = (left + right) // 2
        partition_elements = []
        if is_valid_upperbound(bids, m, mid, partition_elements):
            supremum = mid
            best_partition = partition_elements 
            right = mid - 1
        else:
            left = mid + 1
    return supremum, best_partition


if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int, input().split())
    bids = list(map(int, input().split()))
    sup, partitions = find_supremum(m, bids)
    final_partition = []

    # 4 4
    # 3 1 1 1일때 1/3으로 쪼개지는 것을 1/1/1/1로 나뉘도록 바꾸어 준다. 
    for idx, (count, part_sum) in enumerate(partitions, 1):
        if count == 1:
            final_partition.append(count)
        else:
            
            while count and len(partitions) - idx + len(final_partition) < m - 1:
                final_partition.append(1)
                count -= 1
            
            if count:
                final_partition.append(count)

    print(sup)
    print(*final_partition)
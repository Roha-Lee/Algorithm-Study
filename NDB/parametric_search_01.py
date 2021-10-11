N, M = map(int, input().split())
lengths = list(map(int, input().split()))

def get_amount(lengths, cur_length):
    return sum([length - cur_length for length in lengths if length > cur_length])

start = 0
end = max(lengths)
best = 0
while start <= end: 
    mid = (end + start) // 2
    amount = get_amount(lengths, mid)
    if amount < M:
        end = mid - 1
    else:
        best = mid
        start = mid + 1

print(best)
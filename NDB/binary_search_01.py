from bisect import bisect_left, bisect_right
N, x = map(int, input().split())
numbers = list(map(int, input().split()))
ans = bisect_right(numbers, x) - bisect_left(numbers, x)
if ans == 0:
    ans -= 1
print(ans)
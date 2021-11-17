# import sys 
# from heapq import heappop, heapify
# if __name__ == '__main__':
#     input = sys.stdin.readline
#     n, m = map(int, input().split())
#     check = [False] * (n+1)
#     problems = [(i, -i) for i in range(1, n+1)]
#     for _ in range(m):
#         a, b = map(int, input().split())
#         problems.append((b, -a))
#     heapify(problems)
#     while problems:
#         _, num = heappop(problems)
#         num = -num
#         if check[num]:
#             continue
#         check[num] = True
#         print(num, end=' ')
#     print()
    

import sys 
from collections import Counter
from operator import itemgetter
input = sys.stdin.readline

n = int(input())
book_list = [input().rstrip() for _ in range(n)]
cntr = Counter(book_list)
book_info = [(val, key) for key, val in cntr.items()]
book_info = sorted(book_info, key=itemgetter(1), reverse=True)
book_info = sorted(book_info, key=itemgetter(0), reverse=False)
print(book_info.pop()[1])


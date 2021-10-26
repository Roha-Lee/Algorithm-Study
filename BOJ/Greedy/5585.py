import sys 
input = sys.stdin.readline
n = int(input())
currencies = [500, 100, 50, 10, 5, 1]
start = 1000 - n
count = 0
for currency in currencies:
    count += start // currency
    start %= currency
print(count)
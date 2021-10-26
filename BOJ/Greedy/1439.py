import sys 
input = sys.stdin.readline
usr_input = input().rstrip()
start = 'a'
cnt = [0, 0]
for letter in usr_input:
    if letter != start:
        start = letter
        cnt[int(letter)] += 1
print(min(cnt))
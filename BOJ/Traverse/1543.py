import sys 
input = sys.stdin.readline
document = input().rstrip()
word = input().rstrip()
d_len = len(document)
w_len = len(word)
loc = 0
count = 0
while loc < d_len:
    res = document.find(word, loc)
    if res == -1:
        break
    else:
        count += 1
        loc = res + w_len
print(count)
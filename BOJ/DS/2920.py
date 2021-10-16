import sys
input = sys.stdin.readline
notes = list(map(int, input().split()))

asc = True
des = True
for i in range(1, len(notes)):
    if notes[i] > notes[i-1]:
        des = False
    elif notes[i] < notes[i-1]:
        asc = False

if asc:
    print('ascending')
elif des:
    print('descending')
else:
    print('mixed')



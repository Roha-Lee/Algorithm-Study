import sys
input = sys.stdin.readline
test_num = int(input())
for _ in range(test_num):
    password = input().rstrip()
    left = []
    right = []
    for letter in password:
        if '<' == letter:
            if left:
                right.append(left.pop())
        elif '>' == letter:
            if right:
                left.append(right.pop())
        elif '-' == letter:
            if left:
                left.pop()
        else:
            left.append(letter)
    while right:
        left.append(right.pop())
    
    print(''.join(left)) 
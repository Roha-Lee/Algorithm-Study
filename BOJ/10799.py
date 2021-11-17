import sys 
def get_num_of_bars(pattern):
    curr_bars = 1
    curr = prev = pattern[0]
    total_bars = 0
    for i in range(1, len(pattern)):
        curr = pattern[i]
        if curr == '(':
            curr_bars += 1
        elif curr == ')':
            if prev == '(':
                curr_bars -= 1
                total_bars += curr_bars
            if prev == ')':
                total_bars += 1
                curr_bars -= 1
        prev = curr
    return total_bars


if __name__ == '__main__':
    input = sys.stdin.readline
    pattern = input().rstrip()
    print(get_num_of_bars(pattern))

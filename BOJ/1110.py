import sys 
def count_num_cycle(num): 
    count = 0 
    num1, num2 = num//10, num%10
    start1, start2 = num1, num2
    while not(start1 == num1 and start2 == num2 ) or not count:
        sum_ = num1 + num2 
        num1 = num2
        num2 = sum_ % 10
        count += 1
    return count
if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    print(count_num_cycle(n))
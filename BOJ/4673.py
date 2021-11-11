import sys 
def get_digit(num):
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10
    return digits

def find_self_num():
    check = [True] * 10001
    check[0] = False
    for num in range(1, 10001):
        index = sum(get_digit(num)) + num
        if index <= 10000:
            check[index] = False
    
    self_nums = []
    for i, val in enumerate(check):
        if val:
            self_nums.append(i)

    return self_nums

    
if __name__ == '__main__':
    input = sys.stdin.readline
    self_nums = find_self_num()
    for num in self_nums:
        print(num)
import sys 
input = sys.stdin.readline
TABLE = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'a': 10,
    'b': 11,
    'c': 12,
    'd': 13,
    'e': 14,
    'f': 15,
}
def convert(num, base):
    result = 0
    mult = 1
    for digit in num[::-1]:
        result += TABLE[digit.lower()] * mult
        mult *= base
    return result

if __name__ == '__main__':
    num = input().strip()
    if num.startswith('0x'):
        result = convert(num[2:], 16)
    elif num.startswith('0'):
        result = convert(num[1:], 8)
    else:
        result = int(num)
    print(result)
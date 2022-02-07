import sys 
input = sys.stdin.readline
def find_hidden_sum(query):
    result = 0 
    number = ''
    for letter in query + '.':
        if letter.isdigit():
            number += letter 
        else:
            if number:
                result += int(number)
                number = ''
    return result 

if __name__ == '__main__':
    _ = input()
    user_str = input().strip()
    print(find_hidden_sum(user_str))
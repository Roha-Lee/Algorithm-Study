# TODO
import sys

from itertools import combinations_with_replacement, chain
def is_valid_eqn(eqn):
    parenthesis = []
    
    for letter in eqn:
        if letter == '(':
            parenthesis.append(1)
        elif letter == ')':
            parenthesis.pop()
    
    if parenthesis:
        return True
    return False

def is_valid_parenthesis(open_cass, close_case):
    if not len(open_cass) == len(close_case):
        return False
    
    for op, cl in zip(open_cass, close_case):
        if not op < cl:
            return False
    return True

def find_max_value(n, eqn):
    par_num = n // 2
    open_par = []
    close_par = []
    for i in range(1, par_num + 1):
        open_par.extend(list(combinations_with_replacement(range(par_num + 1), i)))
        close_par.extend(list(combinations_with_replacement(range(1, par_num + 1), i)))
    count = 0 
    for open_case in open_par:
        for close_case in close_par:
            if is_valid_parenthesis(open_case, close_case):
                count += 1
    print(count)
if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    equation = input().rstrip()
    print(find_max_value(n, equation))
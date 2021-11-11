import sys 
from collections import deque
from operator import add, sub, mul
def get_max_answer_of_eqn(eqn, idx, subtotal=0):
    global total_max
    if idx == len(eqn):
        total_max = max(subtotal, total_max)
        return 
    
    op1 = op_dict[eqn[idx]]
    result1 = op1(subtotal , int(eqn[idx+1]))
    get_max_answer_of_eqn(eqn, idx + 2, result1)

    if idx + 3 < len(eqn):
        op2 = op_dict[eqn[idx+2]]
        result2 = op2(int(eqn[idx+1]), int(eqn[idx+3]))
        result2 = op1(subtotal, result2)
        get_max_answer_of_eqn(eqn, idx + 4, result2)
    
if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    eqn = list(input().rstrip())
    
    total_max = -float("inf")
    
    op_dict = {
        '+': add,
        '-': sub, 
        '*': mul
    }
    get_max_answer_of_eqn(eqn, 1, int(eqn[0]))
    print(total_max)

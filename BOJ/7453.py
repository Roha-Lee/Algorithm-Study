import sys 


def generate_possible_case(A, B):
    result = dict()
    for numA in A:
        for numB in B:
            temp = numA + numB
            if temp in result:
                result[temp] += 1
            else:
                result[temp] = 1
    return result

def count_sum_zero_pair(A, B, C, D):
    left_possible = generate_possible_case(A, B)
    
    count = 0 
    for numC in C:
        for numD in D:
            temp = numC + numD
            if -temp in left_possible:
                count += left_possible[-temp]
        
    return count 
    
if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    A, B, C, D = [], [], [], []
    for i in range(n):
        a, b, c, d = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)
        
    print(count_sum_zero_pair(A, B, C, D))
    
    
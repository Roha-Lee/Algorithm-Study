import sys 
input = sys.stdin.readline
if __name__ == '__main__':
    N, M = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    a_idx, b_idx = 0, 0
    result = []
    while a_idx < len(a_list) and b_idx < len(b_list):
        if a_list[a_idx] < b_list[b_idx]:
            result.append(a_list[a_idx])
            a_idx += 1
        else:
            result.append(b_list[b_idx])
            b_idx += 1
    while a_idx < len(a_list):
        result.append(a_list[a_idx])
        a_idx += 1
    
    while b_idx < len(b_list):
        result.append(b_list[b_idx])
        b_idx += 1
    
    print(*result)
    
        
        



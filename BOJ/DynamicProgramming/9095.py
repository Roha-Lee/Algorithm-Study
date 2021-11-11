import sys 
def count_1_2_3(num):
    DP = [0] * max(num + 1, 2)
    DP[0] = 1
    DP[1] = 1

    for i in range(2, num+1):
        for j in [1,2,3]:
            DP[i] += DP[i-j] if i>=j else 0
    return DP[-1] 

if __name__ == '__main__':
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(count_1_2_3(n))

import sys 
input = sys.stdin.readline
if __name__ == '__main__':
    N, K = map(int, input().split())
    words = [input().strip() for _ in range(N)]
    
    for word in words:
        print(len(set(word)))


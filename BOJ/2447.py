import sys 
def make_star(n):
    if n == 1:
        return ["*"]
    
    make_star(n // 3)
    
if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    letter = '**** ****'
    make_star(n)
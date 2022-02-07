import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    set1 = set(map(int, input().split()))
    set2 = set(map(int, input().split()))
    print(len(set1) + len(set2) - 2 * len(set1.intersection(set2)))

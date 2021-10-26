import sys 
input = sys.stdin.readline
n = int(input())
def n_queen(x):
    global results
    if x == n:
        results += 1
    else:
        for col in range(n):
            if col not in used:
                val1 = x + col
                val2 = x - col + n - 1
                if not diag1[val1] and not diag2[val2]:
                    diag1[val1] = True
                    diag2[val2] = True
                    used.add(col)
                    n_queen(x+1)
                    used.remove(col)
                    diag1[val1] = False
                    diag2[val2] = False
                    
                
used = set()
diag1 = [False] * (2*n-1)
diag2 = [False] * (2*n-1)
results = 0
n_queen(0)
print(results)

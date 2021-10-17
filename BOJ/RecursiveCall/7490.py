import sys 
input = sys.stdin.readline
test_num = int(input())

def make_zero(n, ops):
    if len(ops) == n-1:
        eqn = ''
        for i in range(1, n):
            eqn = eqn + str(i) + ops[i-1]
        eqn += str(n)
        if eval(eqn.replace(' ','')) == 0:
            print(eqn)
        return 
    operations = [' ','+','-']
    for op in operations:
        ops.append(op)
        make_zero(n, ops)
        ops.pop()

for _ in range(test_num):
    max_num = int(input())
    make_zero(max_num, [])
    print()
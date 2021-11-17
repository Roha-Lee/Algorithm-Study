import sys 
def quad_tree_compression(n, data, x, y):
    if n == 1:
        return str(data[x][y])
    
    lt = quad_tree_compression(n//2, data, x, y)
    rt = quad_tree_compression(n//2, data, x, y + n//2)
    lb = quad_tree_compression(n//2, data, x + n//2, y)
    rb = quad_tree_compression(n//2, data, x + n//2, y + n//2)

    if lt == rt and rt == lb and lb == rb and rb == lt and len(lt) + len(rt) + len(lb) + len(rb) == 4:
        return lt
    else:
        return '(%s%s%s%s)'%(lt , rt, lb, rb)

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    data = []
    for i in range(n):
        data.append(list(map(int, input().rstrip())))
    print(quad_tree_compression(n, data, 0, 0))

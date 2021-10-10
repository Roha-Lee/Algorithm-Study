# 유클리드 호제법 
def GCD(A, B):
    if B == 0:
        return A
    if A < B:
        A, B = B, A 
    R = A % B
    return GCD(B, R)

if __name__ == '__main__':
    print(GCD(192, 162))
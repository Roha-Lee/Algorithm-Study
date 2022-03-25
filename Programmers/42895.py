def solution(N, number):
    DP = [set() for _ in range(9)]
    for i in range(1, 9):
        DP[i].add(int(str(N) * i))
        for j in range(1, i):
            for num1 in list(DP[i-j]):
                for num2 in list(DP[j]):
                    DP[i].add(num1 + num2)
                    DP[i].add(num1 - num2)
                    DP[i].add(num1 * num2)
                    if num2: DP[i].add(num1 // num2)
        if number in DP[i]: return i
    return -1
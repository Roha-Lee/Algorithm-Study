# # 1. 모든 필요한 소수 구하기 - 에라토스테네스 체 
# import math 
# import sys 
# input = sys.stdin.readline

# N = int(input())
# upperbound = int(math.sqrt(N))
# sieve = [True] * (N + 1)
# for num in range(2, upperbound):
#     if sieve[num]:
#         for j in range(num * 2, N + 1, num):
#             sieve[j] = False
# primes = [num for num in range(2, N + 1) if sieve[num]]

# # 2. 작은 소수부터 나누어 가면서 결과 리스트에 추가 
# result = []
# user_num = N
# while N >= 2:
#     for prime_num in primes:
#         if N % prime_num == 0:
#             N /= prime_num
#             result.append(prime_num)
#             break

# # 3. 출력
# if not user_num == 1:
#     print(*result, sep='\n')


# naive 
N = int(input())
user_input = N
result = []
while user_input!=1:
    for i in range(2, user_input+1):
        if user_input%i==0:
            result.append(i)
            user_input = int(user_input/i)
            break
if not N == 1:
    print(*result, sep='\n')
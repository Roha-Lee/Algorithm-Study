import math 
def is_prime_number_naive(x):
    for num in range(2, x):
        if x%num == 0:
            return False
    return True

def is_prime_number(x):
    up_bound = math.sqrt(x)
    for num in range(2, math.ceil(up_bound)):
        if x%num == 0:
            return False
    return True

def eratosthenes_sieve_naive(x):
    num_list = [i for i in range(2, x+1)]
    curr = 0
    while curr < len(num_list):
        div = num_list[curr]
        for i in range(len(num_list)-1, -1, -1):
            if num_list[i] != div and num_list[i] % div == 0:
                num_list.pop(i)
        curr += 1
    return num_list

def eratosthenes_sieve(x):
    prime = [True] * (x+1)
    for i in range(2, math.ceil(math.sqrt(x))):
        if prime[i]:
            j = 2
            while i * j <= x:
                prime[i * j] = False
                j += 1
    return prime


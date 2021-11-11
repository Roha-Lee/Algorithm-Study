import sys 
from itertools import permutations
def from_num_to_result(answer, num):
    strike = [n1 == n2 for n1, n2 in zip(answer, num)]
    ball = [digit in answer for digit in num]
    return sum(strike), sum(ball) - sum(strike)
    
def get_candidates_with_response(responses, possibles):
    count = 0 
    for possible in possibles:
        for strike, ball, candidate in responses:
            if strike == 3:
                return 1
            cstrike, cball = from_num_to_result(possible, candidate)
            if not (strike == cstrike and ball == cball):
                break
        else:
            count += 1
    return count

if __name__ == '__main__':
    input = sys.stdin.readline
    ans = int(input())
    responses = []
    possibles = permutations(range(1, 10), 3)
    for _ in range(ans):
        candidate, strike, ball = input().split()
        strike = int(strike)
        ball = int(ball)
        candidate = list(map(int, candidate))
        responses.append((strike, ball, candidate))
    responses = sorted(responses)
    print(get_candidates_with_response(responses, possibles))


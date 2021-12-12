from math import gcd, lcm
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        gcd_a_b = gcd(a, b)
        lcm_a_b = lcm(a, b)
        a_part, b_part = lcm_a_b // b, lcm_a_b // a
        seq_len = a_part + b_part - 1
        
        quotient, remainder = (n-1) // seq_len, (n-1) % seq_len
        
        candidates = []
        for k in range(1, a_part):
            candidates.append(b * k)
        for k in range(1, b_part+1):
            candidates.append(a * k)
        return (quotient * lcm_a_b + sorted(candidates)[remainder]) % (10**9 + 7)
            
        
        
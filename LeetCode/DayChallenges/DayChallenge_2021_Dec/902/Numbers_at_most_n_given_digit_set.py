from bisect import bisect_left
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        order = 0
        n_copy = n
        len_digits = len(digits)
        digits = [int(digit) for digit in digits]
        
        total_count = 0
        count_base = 1
        while n_copy > 9:
            count_base *= len_digits
            total_count += count_base
            n_copy //= 10

            # case - use full slot of number
        for curr in str(n):
            curr = int(curr)
            digit_num = bisect_left(digits, curr)
            total_count += digit_num * count_base
            
            if curr not in digits: 
                break

            count_base //= len_digits
        
        if not count_base and n % 10 in digits:
            total_count += 1
            
        return total_count

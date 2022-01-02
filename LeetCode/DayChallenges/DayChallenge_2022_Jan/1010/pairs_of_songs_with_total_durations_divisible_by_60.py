from collections import Counter
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        sixties = [60*i for i in range(1, 17)]
        durations = Counter(time)
        
        count = 0
        min_d, max_d = min(time), max(time)
        
        for idx, song in enumerate(time):
            for sixty in sixties:
                remainder = sixty - song
                if remainder < min_d or remainder > max_d:
                    continue
                if remainder in durations:
                    if song == remainder:
                        if durations[remainder] == 1:
                            continue
                        else:
                            count -= 1
                    count += durations[remainder]
        return count // 2
        
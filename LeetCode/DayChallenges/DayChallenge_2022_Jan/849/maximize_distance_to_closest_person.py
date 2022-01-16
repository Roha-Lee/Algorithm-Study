class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        zeros, internal = 0, 0
        for idx, seat in enumerate(seats):
            if seat:
                internal = max(zeros, internal)
                zeros = 0
            else:
                zeros += 1
       
        from_start, from_end = 0, 0
        while not seats[from_start]:
            from_start += 1
            
        while not seats[-from_end-1]:
            from_end += 1
            
        return max(from_start, from_end, (internal+1) // 2)
            
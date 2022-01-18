class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        from_start, from_end = 0, 0
        while from_start < len(flowerbed) and not flowerbed[from_start]:
            from_start += 1
        while from_end < len(flowerbed) and not flowerbed[-from_end-1]:
            from_end += 1
        if from_start == len(flowerbed):
            return n <= (from_start + 1) // 2
        total_slot, cnt = 0, 0
        for i in range(from_start, len(flowerbed)):
            if flowerbed[i]:
                if cnt > 0:
                    total_slot += (cnt -1) // 2
                cnt = 0
            else:
                cnt += 1
        return total_slot + from_start // 2 + from_end // 2 >= n
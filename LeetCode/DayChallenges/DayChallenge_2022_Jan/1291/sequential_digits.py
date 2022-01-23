class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        numbers = "123456789"
        result = []
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)+1):
                num = int(numbers[i:j])
                if low <= num <= high:
                    result.append(num)
        return sorted(result)
            
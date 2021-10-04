class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seq_table = dict()
        for i in range(0, len(s)-9):
            sliced = s[i:i+10]
            seq_table.setdefault(sliced, 0)
            seq_table[sliced] += 1
        results = []
        for k, v in seq_table.items():
            if v > 1:
                results.append(k)                
        return results
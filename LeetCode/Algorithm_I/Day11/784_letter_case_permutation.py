class Solution:
    def _generate(self, s, i, results):
        if len(i) == len(s):
            results.append(i)
            return 
        loc = len(i)
        if s[loc].isalpha():
            self._generate(s, i+s[loc].upper(), results)
            self._generate(s, i+s[loc].lower(), results)
        else:
            self._generate(s, i+s[loc], results)
    def letterCasePermutation(self, s: str) -> List[str]:
        results = []
        self._generate(s, "", results)
        return results
        
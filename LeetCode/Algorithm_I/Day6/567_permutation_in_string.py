from collections import deque
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        if len2 < len1:
            return False
        _dict1 = dict()
        for letter in s1:
            _dict1.setdefault(letter, 0)
            _dict1[letter] += 1
        
        _dict2 = dict()
        let_q = deque()
        for letter in s2[:len1]:
            _dict2.setdefault(letter, 0)
            _dict2[letter] += 1
            let_q.append(letter)
            
        if _dict1 == _dict2:
            return True
        
        for letter in s2[len1:]:
            prev = let_q.popleft()
            _dict2[prev] -= 1
            if _dict2[prev] == 0:
                del _dict2[prev]
                
            _dict2.setdefault(letter, 0)
            _dict2[letter] += 1
            let_q.append(letter)
            if _dict1 == _dict2:
                return True
        return False
                
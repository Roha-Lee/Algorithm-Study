import random
class RandomizedSet:

    def __init__(self):
        self._set = set()

    def insert(self, val: int) -> bool:
        ret = val not in self._set
        if ret:
            self._set.add(val)
        return ret

    def remove(self, val: int) -> bool:
        ret = val in self._set
        if ret:
            self._set.remove(val)
        return ret
        
    def getRandom(self) -> int:
        curr = random.randint(0, len(self._set) - 1)
        return tuple(self._set)[curr]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

import random
class RandomizedSet:

    def __init__(self):
        self._set = set()
        self._data = []
        self._loc = dict()
        self.last = 0

    def insert(self, val: int) -> bool:
        ret = val not in self._set
        if ret:
            self._set.add(val)
            self._data.append(val)
            self._loc[val] = self.last
            self.last += 1
        return ret

    def remove(self, val: int) -> bool:
        ret = val in self._set
        if ret:
            self._set.remove(val)
            data_loc = self._loc[val]
            self._loc[self._data[self.last-1]] = data_loc
            self._data[data_loc], self._data[self.last-1] = self._data[self.last-1], self._data[data_loc]
            self._data.pop()
            self.last -= 1
        return ret
        
    def getRandom(self) -> int:
        curr = random.randint(0, len(self._set) - 1)
        return self._data[curr]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

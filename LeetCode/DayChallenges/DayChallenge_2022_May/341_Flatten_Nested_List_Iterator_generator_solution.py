# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def flatten_list(nested_list):
            for elem in nested_list:
                if elem.isInteger():
                    yield elem.getInteger()
                else:
                    yield from flatten_list(elem.getList())
        self.generator = flatten_list(nestedList)
        self.next_integer = next(self.generator, None)
        
    def next(self) -> int:
        result = self.next_integer
        self.next_integer = next(self.generator, None)
        return result
    
    def hasNext(self) -> bool:
        return self.next_integer is not None
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
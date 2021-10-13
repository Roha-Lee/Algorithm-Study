# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ser = []
        q = deque()
        q.append(root)
        while q:
            curr = q.popleft()
            if curr is None:
                ser.append(None)
                continue
            ser.append(curr.val)
            q.append(curr.left)
            q.append(curr.right)
        
        
        for i in range(len(ser)-1, -1, -1):
            if ser[i] == None:
                ser.pop()
            else:
                break
                
        ser = [str(elem) for elem in ser]
        return ','.join(ser)
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return 
        
        data = data.split(',')
        root = TreeNode(data[0])
        idx = 1
        q = deque()
        q.append(root)
        while q:
            curr = q.popleft()
            if idx < len(data):
                if data[idx] == 'None':
                    curr.left = None
                else:
                    curr.left = TreeNode(int(data[idx]))
                    q.append(curr.left)
                idx += 1
            if idx < len(data):
                if data[idx] == 'None':
                    curr.right = None
                else:
                    curr.right = TreeNode(int(data[idx]))
                    q.append(curr.right)
                idx += 1

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
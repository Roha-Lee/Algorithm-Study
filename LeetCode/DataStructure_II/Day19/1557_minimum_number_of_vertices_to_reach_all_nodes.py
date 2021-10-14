class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        from_nodes = set()
        to_nodes = set()
        for from_node, to_node in edges:
            from_nodes.add(from_node)
            to_nodes.add(to_node)
        return list(from_nodes - to_nodes)
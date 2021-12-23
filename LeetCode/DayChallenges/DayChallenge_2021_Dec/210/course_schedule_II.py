from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        inward_count = {course:0 for course in range(numCourses)}
        for next_course, prev_course in prerequisites:
            graph[prev_course].append(next_course)
            inward_count[next_course] += 1
        q = deque()
        for key, val in inward_count.items():
            if val == 0:
                q.append(key)
                
        result = []
        while q:
            curr = q.popleft()
            result.append(curr)
            for nb in graph[curr]:
                inward_count[nb] -= 1
                if inward_count[nb] == 0:
                    q.append(nb)
        if len(result) == numCourses:
            return result
        return []
                
        
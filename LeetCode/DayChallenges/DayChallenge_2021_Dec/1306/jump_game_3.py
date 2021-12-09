from collections import deque 
class Solution:    
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True
        q = deque([start])
        n = len(arr)
        visited = [False] * n
        visited[start] = True
        
        while q:
            curr = q.popleft()
            if 0 <= curr + arr[curr] < n and not visited[curr + arr[curr]]:
                if arr[curr + arr[curr]] == 0:
                    return True
                q.append(curr + arr[curr])
                visited[curr + arr[curr]] = True
            if 0 <= curr - arr[curr] < n and not visited[curr - arr[curr]]:
                if arr[curr - arr[curr]] == 0:
                    return True
                q.append(curr - arr[curr])
                visited[curr - arr[curr]] = True

        return False

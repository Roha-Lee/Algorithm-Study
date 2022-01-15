from collections import deque, defaultdict
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        next_map = defaultdict(list)
        for idx, num in enumerate(arr):
            next_map[num].append(idx)
            
        q, temp = deque(), deque([(len(arr) - 1, arr[len(arr) - 1])])
        
        visited = [False] * len(arr)
        visited[-1] = True
        cnt = 0 
        
        while q or temp:
            q, temp = temp, q
            cnt += 1   
            while q:
                idx, num = q.popleft()
                
                for n_idx in [idx-1, idx+1] + next_map[num]:
                    if 0 <= n_idx < len(arr) and not visited[n_idx]:
                        if n_idx == 0:
                            return cnt
                        temp.append((n_idx, arr[n_idx]))
                        visited[n_idx] = True
             
    
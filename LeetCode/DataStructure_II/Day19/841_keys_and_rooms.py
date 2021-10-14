class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = []
        q.extend(rooms[0])
        visited = [False] * len(rooms)
        visited[0] = True
        while q:
            room = q.pop()
            if not visited[room]:
                visited[room] = True
                q.extend(rooms[room])
        for visit in visited:
            if visit == False:
                return False
        return True
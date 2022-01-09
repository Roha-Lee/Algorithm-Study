class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        move = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        curr = [0, 0]
        idx = 0

        for letter in instructions:
            if letter == "L":
                idx = (idx + 1) % 4
            elif letter == "R":
                idx = (idx - 1) % 4
            else:
                dx, dy = move[idx]
                curr[0], curr[1] = curr[0] + dx, curr[1] + dy

        return curr == [0, 0] or idx != 0
            
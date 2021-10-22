class Solution:
    def _flood_fill(self, image, sr, sc, start_color, new_color):
        if image[sr][sc] == new_color:
            return
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        row = len(image)
        col = len(image[0])
        image[sr][sc] = new_color
        for dr, dc in moves:
            nr, nc = sr + dr, sc + dc
            if -1 < nr and nr < row and -1 < nc and nc < col:
                if image[nr][nc] == start_color: 
                    self._flood_fill(image, nr, nc, start_color, new_color)
                    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self._flood_fill(image, sr, sc, image[sr][sc], newColor)
        return image
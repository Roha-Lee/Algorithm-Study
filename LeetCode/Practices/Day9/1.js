/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} color
 * @return {number[][]}
 */
 var floodFill = function(image, sr, sc, color) {
    const target = image[sr][sc];
    const move = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    const rows = image.length;
    const cols = image[0].length;
    const q = [[sr, sc]];
    const visit = Array.from(Array(rows), () => new Array(cols).fill(false));
    visit[sr][sc] = true;
    while (q.length) {
        const [currR, currC] = q.pop();
        image[currR][currC] = color;
        for (let [dr, dc] of move) {
            const [nr, nc] = [dr + currR, dc + currC];
            if (0 > nr || rows <= nr || 0 > nc || cols <= nc) continue;
            if (target === image[nr][nc] && !visit[nr][nc]) {
                q.push([nr, nc]);
                visit[nr][nc] = true;
            }
        }
    }
    return image;
};
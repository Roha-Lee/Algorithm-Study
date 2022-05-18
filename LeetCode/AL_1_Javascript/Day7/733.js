/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} newColor
 * @return {number[][]}
 */
 var floodFill = function(image, sr, sc, newColor) {
    const numRow = image.length;
    const numCol = image[0].length;
    const targetColor = image[sr][sc];
    const dR = [1, 0, -1, 0];
    const dC = [0, 1, 0, -1];
    const visited = Array.from(Array(numRow), () => new Array(numCol).fill(false));
    let q = [[sr, sc]];
    let nextQ = [];
    let nR;
    let nC;
    image[sr][sc] = newColor;
    visited[sr][sc] = true;
    while(q.length > 0) {
        for(const [r, c] of q) {
           for(let i = 0; i < 4; i += 1) {
               nR = r + dR[i];
               nC = c + dC[i];
               if(0 > nR || nR >= numRow || 0 > nC || nC >= numCol) continue;
               if(!visited[nR][nC] && image[nR][nC] === targetColor) {
                   image[nR][nC] = newColor;
                   visited[nR][nC] = true;
                   nextQ.push([nR, nC]);
               }
           }
        }
        q = nextQ;
        nextQ = [];
    }
    return image;
};
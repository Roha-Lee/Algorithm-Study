/**
 * @param {number} m
 * @param {number} n
 * @param {number} maxMove
 * @param {number} startRow
 * @param {number} startColumn
 * @return {number}
 */
 var findPaths = function(m, n, maxMove, startRow, startColumn) {
    let dx = [[0,1],[1,0],[0,-1],[-1,0]];
    const cache = {};
    return dfs(startRow,startColumn,0) % 1000000007n;
    
    function dfs(row,col,move){
        let cacheKey = row + "_" + col + "_" + move;
        if(cache[cacheKey]!==undefined){
            return cache[cacheKey];
        }
        if(move>maxMove){
            return 0n;
        }
        if(row>=m || col>=n || row<0 || col<0){
            return 1n;
        }
        let count=0n;
        for(let d=0;d<dx.length;d++){
            count+=dfs(row+dx[d][0],col+dx[d][1],move+1);
        }
        cache[cacheKey]=count;
        return count;
    }
};
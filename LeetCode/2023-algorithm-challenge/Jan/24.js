/**
 * @param {number[][]} board
 * @return {number}
 */
var snakesAndLadders = function(board) {
    const n = board.length;
    const visited = new Array(n * n).fill(false);
    const flatBoard = getFlattenBoard(board);
    let result = 0;
    let currQueue = [1];
    let nextQueue = [];
    let curr;
    while (currQueue.length) {
        result += 1;
        while (currQueue.length) {
            curr = currQueue.shift();
            for (let next = curr + 1; next <= Math.min(curr + 6, n*n); next += 1) {
                if (visited[next]) {
                    continue;
                }
                visited[next] = true;
                let nextPos = next;
                if (flatBoard[next] > -1) {
                    nextPos = flatBoard[nextPos];
                }
                if (nextPos === (n * n)) {
                    return result; 
                }
                nextQueue.push(nextPos);
            }   
        }
        currQueue = nextQueue;
        nextQueue = [];
    }
    return -1;
};

const getFlattenBoard = (board) => {
    let flatBoard = [-1];
    const n = board.length;
    board.reverse();
    for (let i = 0; i < n; i += 1) {
        const isReverse = (i % 2) === 1;
        const row = isReverse ? board[i].reverse() : board[i];
        flatBoard = [...flatBoard, ...row];
    }
    return flatBoard;
}

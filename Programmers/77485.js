function rotation(board, x1, y1, x2, y2) {
    let prev = board[x1][y1];
    let temp;
    let min = prev;
    // top
    for(let y = y1+1; y <= y2; y++){
        temp = board[x1][y];
        board[x1][y] = prev;
        prev = temp;
        min = Math.min(min, prev);   
    }
    
    // right
    for(let x = x1+1; x <= x2; x++){
        temp = board[x][y2];
        board[x][y2] = prev;
        prev = temp;
        min = Math.min(min, prev);
    }
    // bottom
    for(let y = y2-1; y >= y1; y--){
        temp = board[x2][y];
        board[x2][y] = prev;
        prev = temp;
        min = Math.min(min, prev);
    }
    // left
    for(let x = x2-1; x >= x1; x--){
        temp = board[x][y1];
        board[x][y1] = prev;
        prev = temp;
        min = Math.min(min, prev);
    }
    return min;
}

function solution(rows, columns, queries) {
    let board = [];
    let answer = [];
    for(let row = 0; row < rows; row += 1) {
        const rowArray = [];
        for(let col = 0; col < columns; col += 1) {
            rowArray.push(row * columns + col + 1);
        }
        board.push(rowArray);
    }
    for(let i = 0; i < queries.length; i += 1) {
        const [x1, y1, x2, y2] = queries[i];
        answer.push(rotation(board, x1-1, y1-1, x2-1, y2-1));
    }
    
    return answer;
}
/**
 * @param {character[][]} board
 * @return {boolean}
 */
 var isValidSudoku = function(board) {
    const BOARD_SIZE = 9;
    const row_check = Array.from(Array(BOARD_SIZE), () => new Set());
    const col_check = Array.from(Array(BOARD_SIZE), () => new Set());
    const block_check = Array.from(Array(BOARD_SIZE), () => new Set());
    let block;
    let curr;
    
    for(let row = 0; row < BOARD_SIZE; row += 1) {
        for(let col = 0; col < BOARD_SIZE; col += 1) {
            curr = board[row][col];
            block = Math.floor(row / 3) * 3 + Math.floor(col/ 3);
            if (curr === '.') continue;
            if(row_check[row].has(curr)) return false;
            if(col_check[col].has(curr)) return false;
            if(block_check[block].has(curr)) return false;
            row_check[row].add(curr);
            col_check[col].add(curr);
            block_check[block].add(curr);
        }
    }
    return true;
};
// 문제를 정말 잘 읽어야 한다. 
// 자물쇠의 돌기와 열쇠의 돌기가 만나면 안된다는 조건을 간과하여 오래걸렸다. 
function canOpen(key, needKey, dr, dc, numLock) {
    const keyRow = key.length;
    const keyCol = key[0].length;
    const needKeyRow = needKey.length;
    const needKeyCol = needKey[0].length;
    let sum = 0;
    let nr, nc;
    for(let r = 0; r < keyRow; r++){
        for(let c = 0; c < keyCol; c++){
            nr = r + dr;
            nc = c + dc;
            if(nr < 0 || nr >= needKeyRow || nc < 0 || nc >= needKeyCol){
                continue;
            }
            if(key[r][c] === 1 && needKey[nr][nc] === 0){
                return false;
            }
            sum += (key[r][c] === 1 && needKey[nr][nc] === 1) ? 1 : 0;
        }
    }
    return sum === numLock;
}


function rotate90(key){
    const row = key.length;
    const col = key[0].length
    const result = Array.from(Array(row), () => Array(col).fill(0));
    for(let r = 0; r < row; r++){
        for(let c = 0; c < col; c++){
            result[r][c] = key[c][row-r-1];
        }
    }
    return result;
}


function solution(key, lock) {
    const needKey = lock.map(row => {
        return row.map(item => 1-item)
    });
    const numLock = needKey.reduce((prev, curr) => {
        return prev + curr.reduce((p, c) => {
            return p + c;
        }, 0)
    }, 0);
    const numKey = key.reduce((prev, curr) => {
        return prev + curr.reduce((p, c) => {
            return p + c;
        }, 0)
    }, 0)

    if(numLock > numKey){
        return false;
    }
    // key sliding window
    const row = needKey.length;
    const col = needKey[0].length;
    const keyRow = key.length;
    const keyCol = key[0].length;
    let currKey = key;
    for(let i = 0; i < 4; i++){
        currKey = rotate90(currKey);   
        for(let dr = -keyRow + 1; dr < row; dr++){
            for(let dc = -keyCol + 1; dc < col; dc++){
                if(canOpen(currKey, needKey, dr, dc, numLock)){
                    return true;
                }
            }
        }
    }
    return false;
}
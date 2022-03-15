const boardColumn = new Map();

function solution(board, moves) {
    let stack = [-1];
    var answer = 0;
    board.forEach(row => {
        row.forEach((item, index) => {
            if(!boardColumn.hasOwnProperty(index))
                boardColumn[index] = [];
            if(item > 0)
                boardColumn[index].unshift(item);
        })
    })
    moves.forEach(item => {
        const doll = boardColumn[item-1].pop();
        if(!!doll){
            if(stack[stack.length-1] === doll){
                answer += 2;
                stack.pop();
            }
            else{
                stack.push(doll);   
            }   
        }
    })
    return answer;
}
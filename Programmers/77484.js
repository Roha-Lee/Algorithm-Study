function compare(a, b) {
    return b - a;
}

function solution(lottos, winNums) {
    const answer = [];
    let count = 0;
    let unknown = 0;
    const winNumsSet = new Set(winNums);
    for(let i = 0; i < lottos.length; i++){
        if(lottos[i] === 0) {
            unknown += 1;
        }
        if(winNumsSet.has(lottos[i])) {
            count += 1;
        }
    }
    
    return [Math.min(7-count-unknown, 6) , Math.min(7-count, 6)];
}
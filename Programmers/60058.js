function reverseU(p) {
    return p.split('')
        .map(item => item === '(' ? ')': '(')
        .join('');    
}

function solution(p) {
    let answer = '';
    if (p.length === 0) {
        return answer;
    }
    let counter = 0;
    let start = 0;
    let good = true;
    const tempResult = [];
    for(let i = 0; i < p.length; i += 1) {
        if(p[i] === '(') {
            counter += 1;
        }
        else {
            counter -= 1;
            if (counter < 0) {
                good = false;
            }
        }
        if(counter === 0) {
            if (good) {
                tempResult.push(p.slice(start, i + 1));                 
            }
            else {
                tempResult.push(`(${solution(p.slice(i+1))})${reverseU(p.slice(start+1, i))}`);
                return tempResult.join('');
            }
            good = true;
            start = i + 1;
        }
    } 
    return tempResult.join('');
}
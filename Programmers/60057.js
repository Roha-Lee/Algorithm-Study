function compression(s, num) {
    const splitted = [];
    for(let i = 0; i < s.length; i+= num) {
        splitted.push(s.substring(i, i+num));
    }
    let compressed = '';
    let count = 1;
    for(let i = 0; i < splitted.length - 1; i++) {
        if (splitted[i] === splitted[i+1]) {
            count += 1;
        }
        else {
            if(count > 1){
                compressed += count;
                count = 1;
            }
            compressed += splitted[i];
        }
    }
    if(count > 1) {
        compressed += count;
    }
    compressed += splitted[splitted.length-1];
    return compressed.length;
}

function solution(s) {
    let answer = Infinity;
    for(let num = 1; num < s.length/2 + 1; num++){
        answer = Math.min(answer, compression(s, num));
    }
    return answer;
}
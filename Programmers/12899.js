function solution(n) {
    const convertTable = ['4','1','2'];
    let answer = '';
    while(n > 0){
        answer = convertTable[n % 3] + answer;
        n = Math.floor((n -1) / 3);
    }
    return answer;
}
function solution(N) {
    // write your code in JavaScript (Node.js 8.9.4)
    let result = '';
    while(N > 0){
        result = (N % 2) + result;
        N = Math.floor(N / 2);
    }
    let gaps = result.split('1');
    gaps = gaps.slice(1, gaps.length-1);
    return gaps.reduce((prev, curr) => {
        return Math.max(prev, curr.length)
    }, 0)
}
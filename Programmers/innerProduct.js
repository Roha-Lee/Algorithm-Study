function solution(a, b) {
    var answer = a.reduce((prev, curr, idx) => prev + curr * b[idx], 0);
    return answer;
}
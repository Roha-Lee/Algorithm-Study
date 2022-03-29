function solution(array, commands) {
    let answer = [];
    for(let i = 0; i < commands.length; i++) {
        const [start, end, k] = commands[i];
        const sliced = array.slice(start - 1, end);
        sliced.sort((a, b) => a-b);
        answer.push(sliced[k-1]);
    }
    return answer;
}
function solution(numbers, target) {
    let answer = 0;
    const stack = [0];
    function DFS(index) {
        if(numbers.length === index){
            if(target === stack[stack.length - 1]){
                answer += 1;
            }
            return;
        }
        const signs = [1, -1];
        for(let sign of signs){
            stack.push(stack[stack.length -1] + sign * numbers[index]);
            DFS(index + 1);
            stack.pop();
        }
    }
    DFS(0);
    return answer;
}
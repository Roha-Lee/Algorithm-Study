function solution(numbers) {
    return 45 - numbers.reduce((prev, curr) => {
        return prev + curr;
    }, 0);
}
function solution(answers) {
    patterns = ['12345', '21232425', '3311224455'];
    results = [];
    let i = 1;
    for(let pattern of patterns) {
        results.push([i, answers.reduce((prev, curr, index) => {
            return prev + +(curr == pattern[index % pattern.length]);
        }, 0)]);
        i += 1;
    }
    results.sort((a, b) => {
        return b[1] - a[1];
    })
    return results.filter(item => results[0][1] === item[1]).map(item => item[0])
;}
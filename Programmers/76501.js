function solution(absolutes, signs) {
    let answer = 0;
    absolutes.forEach((item, index) => {
      answer += (signs[index] ? 1 : -1) * item;
    })
    return answer;
}
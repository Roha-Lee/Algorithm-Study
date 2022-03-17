function canHandle(candidate, times, targetPeople) {
    let maxPeople = 0;
    times.forEach(time => {
        maxPeople += Math.floor(candidate / time);
    });
    return maxPeople >= targetPeople;
}

function solution(n, times) {
    let answer = 0;
    let mid = 0;
    let left = 1;
    let right = 1000000000000000000;
    while(left <= right){
        mid = Math.floor((left + right) / 2);
        if(canHandle(mid, times, n)){
            answer = mid;
            right = mid - 1;
        }
        else{
            left = mid + 1;
        }
    }
    return answer;
}
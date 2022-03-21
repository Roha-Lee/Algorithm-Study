function strToMilliseconds(time) {
    const [hour, minute, second] = time.split(':').map(item => Number(item));
    return (3600 * hour + 60 * minute + second) * 1000;
}


function compare(a, b) {
    return a[1] === b[1] ? (a[0] < b[0] ? 1 : -1) : a[1] - b[1];    
}


function solution(lines) {
    let answer = 0;
    let timeArray = [];
    let endTime, startTime;
    lines.forEach(line => {
        const [date, time, duration] = line.split(' ');
        endTime = strToMilliseconds(time);
        startTime = endTime - Number(duration.substring(0, duration.length - 1)) * 1000 + 1;
        endTime = endTime + 999;
        timeArray.push(['S', startTime]);
        timeArray.push(['E', endTime]);
    })
    
    timeArray.sort(compare)
    let counter = 0;
    timeArray.forEach(([stamp, ]) => {
        if(stamp === 'S') {
            counter += 1;
        }
        else {
            counter -= 1;
        }
        answer = Math.max(answer, counter);
    })
    return answer;
}
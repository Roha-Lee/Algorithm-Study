function minuteToString(minute) {
    const h = Math.floor(minute / 60);
    const m = minute % 60;
    
    return `${String(h).padStart(2, 0)}:${String(m).padStart(2, 0)}` ;
}

function solution(n, t, m, timetable) {
    const minuteTimetable = timetable.map(item => {
        const [h, m] = item.split(':').map(time => Number(time));
        return h * 60 + m;
    })
    // 시간 순서대로 정렬
    minuteTimetable.sort((a, b) => a-b);
    
    let shuttleTime = 9 * 60;
    let prev;
    let count;
    for(let depart = 0; depart < n; depart++){
        prev = -1;
        count = 0;
        for(let crew = 0; crew < m; crew++){
            if(minuteTimetable[0] <= shuttleTime) {
                prev = minuteTimetable.shift();    
                count += 1;
            }
            else {
                break;
            }
        }
        shuttleTime += t;
    }
    
    if(count < m){
        return minuteToString(shuttleTime - t);
    }
    else{
        return minuteToString(prev - 1);
    }
}
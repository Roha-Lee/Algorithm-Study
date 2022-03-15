const userTable = new Map();

function solution(record) {
    var answer = [];
    record.forEach(item => {
        const [operation, uid, nickname] = item.split(' ');
        if(operation !== 'Leave'){
            userTable[uid] = nickname; 
        }
    })
    record.forEach(item => {
        const [operation, uid, ] = item.split(' ');
        if(operation === 'Leave'){
            answer.push(`${userTable[uid]}님이 나갔습니다.`)
        }
        else if(operation === 'Enter'){
            answer.push(`${userTable[uid]}님이 들어왔습니다.`)
        }
    })

    return answer;
}
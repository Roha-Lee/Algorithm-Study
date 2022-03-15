let reportedCount = {};
let reportList = {};

function solution(id_list, report, k) {
    var answer = [];
    // initialization
    id_list.forEach(item => {
        reportedCount[item] = 0;
        reportList[item] = []
    })
    
    report.forEach(item => {
        const splited = item.split(' ');
        reportList[splited[0]].push(splited[1])
    })
    
    for(let key in reportList){
        reportList[key] = [...(new Set(reportList[key]))]
        reportList[key].forEach(user => {
            reportedCount[user] += 1;
        })
    }
    
    for(let key in reportList){
        answer.push(reportList[key].reduce((prev, curr) => {
            return prev + +(reportedCount[curr] >= k)
        }, 0))
    }
    
    return answer;
}
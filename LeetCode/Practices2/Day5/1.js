/**
 * @param {character[]} tasks
 * @param {number} n
 * @return {number}
 */
 var leastInterval = function(tasks, n) {
    const banned = [];
    const counter = new Map();
    let remain = tasks.length;
    let next;
    let result = 0;
    for (let task of tasks) {
        counter.set(task, (counter.get(task) || 0) + 1);
    }
    
    while (remain > 0) {
        next = getNext(banned, counter);
        if (next !== null) {
            counter.set(next, counter.get(next) - 1);
            remain -= 1;    
        }
        result += 1; 
        if (banned.length >= n) {
            banned.shift();    
        }
        banned.push(next);
    }
    return result;
};

function getNext(banned, counter) {
    let result = null;
    let maxRemain = 0;
    for(let [task, remain] of counter) {
        if (banned.includes(task)) continue;
        if (maxRemain < remain) {
            result = task;
            maxRemain = remain;
        }
    }
    return result;
}
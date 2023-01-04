/**
 * @param {number[]} tasks
 * @return {number}
 */
var minimumRounds = function(tasks) {
    tasks = tasks.sort();
    let result = 0;
    let count = 0;
    let curr = null;
    for (let task of tasks) {
        if (!curr) {
            curr = task; 
            count += 1;
            continue;
        }
        if (curr !== task) {
            if (count === 1) return -1;
            curr = task;
            result += Math.ceil(count / 3);
            count = 1;
        } else {
            count += 1;
        }
    }
    if (count === 1) return -1;
    result += Math.ceil(count / 3);
    return result;
};

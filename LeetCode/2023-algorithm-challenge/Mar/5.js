/**
 * @param {number[]} arr
 * @return {number}
 */
var minJumps = function(arr) {
    const n = arr.length;
    const map = new Map();
    for (let i = 0; i < n; i += 1) {
        let temp = [];
        if (map.has(arr[i])) {
            temp = map.get(arr[i]);    
        }
        temp.push(i);
        map.set(arr[i], temp);
    }
    const visited = new Set();
    let queue = [[0, 0]];
    visited.add(0);

    while(queue.length) {
        let [curr, step] = queue.shift();
        if (curr == n-1) return step;
        if (curr + 1 < n && !visited.has(curr + 1)) {
            queue.push([curr+1, step+1]);
            visited.add(curr + 1);
        }
        if (curr - 1 >= 0 && !visited.has(curr - 1)) {
            queue.push([curr-1, step+1]);
            visited.add(curr - 1);
        }
        for (let i of (map.get(arr[curr]) ?? [])) {
            if (!visited.has(i) && i != curr) {
                queue.push([i, step+1]);
                visited.add(i);
            }
        }
        map.delete(arr[curr]);
    }
    return -1;
};

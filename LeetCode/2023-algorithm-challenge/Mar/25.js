/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var countPairs = function(n, edges) {
    const parents = new Array(n);
    const ranks = new Array(n).fill(1);
    for (let i = 0; i < n; i += 1) {
        parents[i] = i;
    }

    const find = (node) => {
        if (parents[node] === node) return node;
        parents[node] = find(parents[node]);
        return parents[node];
    };

    const union = (node1, node2) => {
        node1 = find(node1);
        node2 = find(node2);
        if (node1 !== node2) {
            if (ranks[node1] >= ranks[node2]) {
                ranks[node1] += 1;
                ranks[node2] = ranks[node1];
                parents[node2] = parents[node1];
            } else {
                ranks[node2] += 1;
                ranks[node1] = ranks[node2];
                parents[node1] = parents[node2];
            }
        }
    };

    for (let [src, dst] of edges) {
        union(src, dst);
    }
    for (let i = 0; i < n; i += 1) {
        find(i);
    }
    const counter = parents.reduce((acc, cur) => {
        if (acc[cur] === undefined) {
            acc[cur] = 1;
        } else {
            acc[cur] += 1;
        }
        return acc;
    }, {});
    
    let result = 0;
    let total = n;
    const values = Object.values(counter);
    for (let i = 0; i < values.length; i += 1) {
        result += values[i] * (total - values[i]);
        total -= values[i];
    }

    return result;
};

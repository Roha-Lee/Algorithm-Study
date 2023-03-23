/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number}
 */
var makeConnected = function(n, connections) {
    let chunk = n;
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
            chunk -= 1;
        }
    };

    let remains = 0;
    const connected = new Set();
    for (let [n1, n2] of connections) {
        const root1 = find(n1);
        const root2 = find(n2);
        if (root1 !== root2) {
            union(n1, n2);    
            connected.add(n1);
            connected.add(n2);
        } else {
            remains += 1;
        }        
    }
    return (chunk - 1) <= remains ? chunk - 1 : -1;
};

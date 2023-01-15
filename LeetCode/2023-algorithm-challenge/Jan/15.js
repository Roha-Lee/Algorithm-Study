/**
 * @param {number[]} vals
 * @param {number[][]} edges
 * @return {number}
 */
var numberOfGoodPaths = function(vals, edges) {
    const n = vals.length;
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
    
    const tree = buildTree(edges);
    const valToNodes = vals.reduce((acc, curr, index) => {
        if (acc.hasOwnProperty(curr)) {
            acc[curr].push(index);            
        } else {
            acc[curr] = [index];
        }
        return acc;
    }, {});

    let result = 0;
    for (let val of Object.keys(valToNodes)) {
        for (let node of valToNodes[val]) {
            for (let neighbor of tree[node] ?? []) {
                if (vals[neighbor] <= vals[node]) {
                    union(node, neighbor);
                }
            }
        }
        const freqOfParent = {};
        let parentNode;
        for (let node of valToNodes[val]) {
            parentNode = find(node);
            if (!freqOfParent.hasOwnProperty(parentNode)) {
                freqOfParent[parentNode] = 0;
            }
            freqOfParent[parentNode] += 1;
        }
        for (let freq of Object.values(freqOfParent)) {
            result += freq * (freq + 1) / 2;
        }
    }
    return result;
};


const buildTree = (edges) => {
    const tree = {};
    for (let [src, dst] of edges) {
        if (tree.hasOwnProperty(src)) {
            tree[src].push(dst);
        } else {
            tree[src] = [dst];
        }
        
        if (tree.hasOwnProperty(dst)) {
            tree[dst].push(src);
        } else {
            tree[dst] = [src];
        }
    }
    return tree;
}

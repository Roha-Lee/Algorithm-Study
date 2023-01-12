/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {string} labels
 * @return {number[]}
 */
var countSubTrees = function(n, edges, labels) {
    const tree = buildTree(edges);
    const result = new Array(n).fill(0);
    const visited = new Array(n).fill(false);
    visited[0] = true;
    const traverse = (node) => {
        let wordCounter = {};
        for (let next of tree[node]) {
            if (visited[next]) continue;
            visited[next] = true;
            const fromChild = traverse(next);
            wordCounter = mergeCounter(wordCounter, fromChild);
        }
        wordCounter = mergeCounter(wordCounter, { [labels[node]]: 1 });
        result[node] = wordCounter[labels[node]] ?? 1;
        return wordCounter;
    }
    traverse(0);
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

const mergeCounter = (acc, curr) => {
    Object.keys(curr).forEach((label) => {
        if (!acc.hasOwnProperty(label)) {
            acc[label] = 0;
        } 
        acc[label] += curr[label];
    });
    return acc;
}
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {boolean[]} hasApple
 * @return {number}
 */
var minTime = function(n, edges, hasApple) {
    const tree = buildTree(edges);
    let time = 0;
    const visited = new Array(n).fill(false);
    visited[0] = true;
    const traverse = (curr) => {
        let child = false;
        for (let next of tree[curr]) {
            if (!visited[next]) {
                visited[next] = true;
                child = traverse(next) || child;
            }
        }
        if (hasApple[curr] || child) {
            time += 2;
            return true;
        }
        return false;
    }
    exist = traverse(0);
    return time - 2 * exist;
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
/**
 * @param {number[]} parent
 * @param {string} s
 * @return {number}
 */
var longestPath = function(parent, s) {
    const tree = buildTree(parent);
    const visited = new Array(s.length).fill(false);
    const traverse = (node) => {
        let canExtendMax = [0, 0];
        let cannotExtendMax = 0;
        
        for (let child of tree[node]) {
            if (visited[child]) continue;
            visited[child] = true;
            let [canExtend, cannotExtend] = traverse(child);
            if (s[child] !== s[node]) {
                if (canExtendMax[0] < canExtend) {
                    canExtendMax[1] = canExtendMax[0];
                    canExtendMax[0] = canExtend;
                } else if (canExtendMax[1] < canExtend) {
                    canExtendMax[1] = canExtend;
                }
            }
            cannotExtendMax = Math.max(cannotExtendMax, cannotExtend);
        }
        return [canExtendMax[0] + 1, Math.max(canExtendMax[0] + canExtendMax[1] + 1, cannotExtendMax)];
    };
    visited[0] = true;
    return Math.max(...traverse(0));
};

const buildTree = (parents) => {
    const tree = {};
    parents.forEach((parent, child) => {
        if (parent === -1) {
            tree[child] = [];
            return;
        }
        if (tree.hasOwnProperty(parent)) {
            tree[parent].push(child);
        } else {
            tree[parent] = [child];
        }
        if (tree.hasOwnProperty(child)) {
            tree[child].push(parent);
        } else {
            tree[child] = [parent];
        }
    });
    return tree;
};

/**
 * @param {string} s1
 * @param {string} s2
 * @param {string} baseStr
 * @return {string}
 */
var smallestEquivalentString = function(s1, s2, baseStr) {
    const parents = new Array(26);
    for (let i = 0; i < 26; i += 1) {
        parents[i] = i;
    }    
    const find = (node) => {
        if (parents[node] === node) return node;
        parents[node] = find(parents[node]);
        return parents[node];
    };
    const union = (node1, node2) => {
        node1 = find(convertCode(node1));
        node2 = find(convertCode(node2));
        if (node1 !== node2) {
            if (node1 >= node2) {
                parents[convertCode(node1)] = convertCode(node2);
            } else {
                parents[convertCode(node2)] = convertCode(node1);
            }
            
        }
    }
    for (let i = 0; i < s1.length; i += 1) {
        union(s1[i], s2[i]);
    }
    let result = "";
    for (let i = 0; i < baseStr.length; i += 1) {
        result += String.fromCharCode(97 + find(convertCode(baseStr[i])));
    }
    return result;
};

const convertCode = (letter) => {
    if (typeof letter === typeof "") {
        return letter.charCodeAt(0) - 97;
    }
    return letter;
}

/**
 * @param {string[]} ideas
 * @return {number}
 */
var distinctNames = function(ideas) {
    const ideaMap = new Map();
    for (let i = 0; i < ideas.length; i += 1) {
        const postFix = ideas[i].slice(1);
        if (ideaMap.has(postFix)) {
            ideaMap.get(postFix).push(ideas[i][0]);
        } else {
            ideaMap.set(postFix, [ideas[i][0]]);
        }
    }
    const ideaMapSummary = new Map();
    const letters = "abcdefghijklmnopqrstuvwxyz";
    for (let [_, v] of ideaMap) {
        for (let i = 0; i < 26; i += 1) {
            for (let j = i + 1; j < 26; j +=1) {
                if (v.includes(letters[i]) ^ v.includes(letters[j])) {
                    const key = letters[i] + letters[j] + Number(v.includes(letters[i]));
                    const curr = ideaMapSummary.get(key) || 0;
                    ideaMapSummary.set(key, curr + 1);
                }
            }
        }
    }    
    let result = 0;
    for (let i = 0; i < 26; i += 1) {
        for (let j = i + 1; j < 26; j += 1) {
            result += 2 * 
                    (ideaMapSummary.get(letters[i] + letters[j] + 0) || 0) * 
                    (ideaMapSummary.get(letters[i] + letters[j] + 1) || 0) ;
        }
    }
    return result;
};

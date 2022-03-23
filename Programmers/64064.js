function findPattern(userId, pattern) {
    return userId
    .filter(id => id.length === pattern.length)
    .filter(id => {
        for(let i = 0; i < pattern.length; i++){
            if(pattern[i] === '*') continue;
            if(pattern[i] !== id[i]) return false;
        }
        return true;
    })       
}

function solution(userId, bannedId) {
    let answer = 0;
    const bannedIdTable = {}
    bannedId.forEach(pattern => {
        bannedIdTable[pattern] = findPattern(userId, pattern);
    });    
    const realBannedId = [];
    const isUsed = {};
    userId.forEach(id => {
        isUsed[id] = false;
    });
    const result = new Set();
    function DFS(index){
        if(index === bannedId.length){
            if(bannedId.length === realBannedId.length) {
                result.add([...realBannedId].sort().join('#'))
            }   
            return;
        } 
        
        for(let id of bannedIdTable[bannedId[index]]){
            if(!isUsed[id]){
                isUsed[id] = true;
                realBannedId.push(id);
                DFS(index + 1);
                isUsed[id] = false;
                realBannedId.pop();
            }
        }
    }
    DFS(0);
    return result.size;
}
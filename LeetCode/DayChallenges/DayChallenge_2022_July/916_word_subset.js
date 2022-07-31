/**
 * @param {string[]} words1
 * @param {string[]} words2
 * @return {string[]}
 */
 var wordSubsets = function(A, B) {
    let inb = {};
    let ina = {};
    let ans = [];
    for(let i = 0 ; i < B.length; i++){
        let word = getFreq(B[i]);
        let key = Object.keys(word);
        for(let j = 0 ; j < key.length; j++){
            if(!inb[key[j]] || inb[key[j]] < word[key[j]]){
                inb[key[j]] = word[key[j]];
            }
        }
    }
    
    let keysInB = Object.keys(inb);
    
    for(let i = 0 ; i < A.length; i++){
        let freq = getFreq(A[i]);
        let flag = true;
        for(let j = 0 ; j < keysInB.length; j++){
            let char = keysInB[j];
            if(!freq[char] ||  freq[char] < inb[char]){
                flag = false;
                break;
            }
        }
        if(flag) ans.push(A[i]);
    }
    return ans;
};

function getFreq(word){
    let ans = {};
    for(let i = 0 ; i < word.length; i++){
        if(ans[word[i]]){
            ans[word[i]]++;
        } 
        else{
            ans[word[i]] = 1;
        }
    }
    return ans;
}
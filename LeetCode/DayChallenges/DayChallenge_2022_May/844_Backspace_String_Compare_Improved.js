/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
 const backspaceCompare = function(s, t) {
    let idxS = s.length - 1;
    let idxT = t.length - 1;
    while(0 <= idxS || 0 <= idxT) {
        let skipS = 0; 
        let skipT = 0
        while(s[idxS] === '#' || skipS > 0) {
            if(s[idxS] === '#') skipS += 1;
            else if (skipS > 0) skipS -= 1;
            idxS -= 1;
        }
        while(t[idxT] === '#' || skipT > 0) {
            if(t[idxT] === '#') skipT += 1;    
            else if (skipT > 0) skipT -= 1;
            idxT -= 1;
        }
        if(s[idxS] !== t[idxT]) return false;
        idxS -= 1;
        idxT -= 1;
    }
    return true;
};

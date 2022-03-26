function jacard(set1, set2) {
    let intersection = 0;
    let union = 0;
    let idx1 = 0, idx2 = 0;
    while (idx1 < set1.length && idx2 < set2.length) {
        if(set1[idx1] === set2[idx2]){  
            intersection += 1;
            idx1 += 1;
            idx2 += 1;
        }
        else if(set1[idx1] < set2[idx2]){
            idx1 += 1;
        }
        else{
            idx2 += 1;
        }
    }
    union = set1.length + set2.length - intersection;
    return intersection / union;
}

function solution(str1, str2) {
    const multiSet1 = [];
    const multiSet2 = [];
    str1 = str1.toLowerCase();
    str2 = str2.toLowerCase();
    for(let i = 0; i < str1.length - 1; i++){
        const piece = str1.slice(i, i+2);
        if (!!piece.match(/[a-z][a-z]/)){
            multiSet1.push(piece);
        }
    }
    for(let i = 0; i < str2.length - 1; i++){
        const piece = str2.slice(i, i+2);
        if (!!piece.match(/[a-z][a-z]/)){
            multiSet2.push(piece);
        }
    }
    if (multiSet1.length === 0 && multiSet2.length === 0){
        return 65536;
    }
    multiSet1.sort();
    multiSet2.sort();
    
    return Math.floor(65536 * jacard(multiSet1, multiSet2));
}
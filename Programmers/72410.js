const allowCharacter = 'abcdefghijklmnopqrstuvwxyz0123456789-_.';
function solution(new_id) {
    const allowCharacterSet = new Set(allowCharacter.split(''));
    // step 1
    let newId = new_id.toLowerCase().split('');
    newId = newId
    // step 2
    .filter(item => allowCharacterSet.has(item)) 
    // step 3
    .reduce((prev, curr) => { 
        if(prev[prev.length - 1] === '.' && curr === '.'){
            return [...prev];
        }
        else{
            return [...prev, curr];           
        }
    }, ['1'])
    .slice(1)
    // step 4
    let start = 0;
    let end = newId.length;
    if(newId.length > 0){
        if(newId[start] === '.'){
            start += 1;
        }
        if(newId[end - 1] === '.'){
            end -= 1;
        }
    }
    newId = newId.slice(start, end)
    // step 5
    if(newId.length === 0){
        newId.push('a');
    }
    // step 6
    if(newId.length >= 16){
        end = 15;
        if(newId[14] === '.'){
            end = 14;
        }
        newId = newId.slice(0, end);
    }
    while(newId.length <= 2){
        newId.push(newId[newId.length-1])
    }
    return newId.join('');
}
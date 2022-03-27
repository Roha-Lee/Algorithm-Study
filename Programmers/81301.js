const words = ['one', 
                 'two', 
                 'three', 
                 'four', 
                 'five', 
                 'six', 
                 'seven', 
                 'eight', 
                 'nine', 
                 'zero'];
const numbers = ['1','2','3','4','5','6','7','8','9','0'];

function solution(s) {
    
    for(let i = 0; i < words.length; i++){
        const re = new RegExp(words[i], 'g');
        s = s.replace(re, numbers[i]);
    }
    return Number(s);
}
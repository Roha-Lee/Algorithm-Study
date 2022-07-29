/**
 * @param {string[]} words
 * @param {string} pattern
 * @return {string[]}
 */
 var generate_pattern = (word) =>{
    let pat_index = 0
    let a = []
    let temp = []
    word.split("").forEach((c,index)=>{
        temp.includes(c)?a.push(temp.indexOf(c)):a.push(pat_index++)
        temp.push(c)
    })
    return a
}
var findAndReplacePattern = function(words, pattern) {
    let p = generate_pattern(pattern)
    let x = words.filter(w=>JSON.stringify(p)==JSON.stringify(generate_pattern(w)))
    return x
};
/**
 * @param {string[]} products
 * @param {string} searchWord
 * @return {string[][]}
 */
 var suggestedProducts = function(products, searchWord) {
    const tries = new Map();
    let curr;
    let next;
    let candidates;
    let index;
    products.forEach(product => {
        curr = tries;
        (product).split("").forEach(letter => {
            next = curr.get(letter) ?? new Map();
            candidates = next.get('candidates') ?? new Array();
            if (next.size === 0) {
                curr.set(letter, next);
                next.set('candidates', candidates);
            }
            index = candidates.findIndex(item => item > product);
            index = index === -1 ? candidates.length : index ;
            candidates.splice(index, 0, product);
            curr = next; 
        });
    });
    curr = tries;
    return searchWord.split("").reduce((prev, letter) => {
        next = curr?.get(letter);
        candidates = next?.get('candidates') ?? new Array();
        prev.push(candidates.slice(0, 3));
        curr = next;
        return prev;
    }, []);
};
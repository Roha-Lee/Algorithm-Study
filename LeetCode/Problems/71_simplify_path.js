/**
 * @param {string} path
 * @return {string}
 */
var simplifyPath = function(path) {
    let result = [];
    path.split('/')
    .filter(item => item !== '')
    .forEach(item => {
        if(item === '..'){
            result?.pop();
        }
        else if(item !== '.'){
            result.push(item);
        }
    })
    
    return result.reduce((prev, curr) => {
        return prev + `/${curr}`;
    }, '') || '/'
    
    
};
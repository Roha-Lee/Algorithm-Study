/*
 * Complete the 'birthday' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY s
 *  2. INTEGER d
 *  3. INTEGER m
 */

function birthday(s, d, m) {
    // Write your code here
    let ways = 0;
    for(let i = 0; i < s.length - m +1; i++) {
        if(s
        .slice(i, i + m)
        .reduce((prev, curr) => {
            return prev + curr;
        }, 0) === d) {
            ways += 1;
        }
    }
    return ways;
}

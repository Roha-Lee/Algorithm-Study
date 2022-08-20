/**
 * @param {string} secret
 * @param {string} guess
 * @return {string}
 */
 var getHint = function(secret, guess) {
    const secrets = new Map();
    const guesses = new Map();
    let bulls = 0;
    let cows = 0;
    for (let i = 0; i < secret.length; i += 1) {
        secrets.set(secret[i], (secrets.get(secret[i]) || 0) + 1);
        guesses.set(guess[i], (guesses.get(guess[i]) || 0) + 1);
        bulls += secret[i] === guess[i];
    }
    for (let [num, count] of guesses) {
        cows += Math.min(secrets.get(num) || 0, count);
    }
    cows -= bulls;
    return `${bulls}A${cows}B`;
};
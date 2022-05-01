/**
 * @param {string} s
 * @return {string[]}
 */
const getWordStack = function (s) {
  const stack = [];
  for (let i = 0; i < s.length; i += 1) {
    if (s[i] !== '#') {
      stack.push(s[i]);
    } else {
      if (stack.length > 0) {
        stack.pop();
      }
    }
  }
  return stack;
};

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
const backspaceCompare = function (s, t) {
  const stackS = getWordStack(s);
  const stackT = getWordStack(t);
  if (stackS.length !== stackT.length) return false;
  for (let i = 0; i < s.length; i += 1) {
    if (stackS[i] !== stackT[i]) return false;
  }
  return true;
};
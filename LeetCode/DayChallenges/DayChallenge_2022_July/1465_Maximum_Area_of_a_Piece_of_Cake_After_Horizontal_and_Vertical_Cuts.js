/**
 * @param {number} h
 * @param {number} w
 * @param {number[]} horizontalCuts
 * @param {number[]} verticalCuts
 * @return {number}
 */
 var maxArea = function(h, w, horizontalCuts, verticalCuts) {
  let maxDeltaHeight = 0;
  let maxDeltaWidth = 0;
  horizontalCuts.sort((a, b) => a > b ? 1 : -1);
  verticalCuts.sort((a, b) => a > b ? 1 : -1);
  [...horizontalCuts ,h].reduce((acc, curr) => {
      maxDeltaHeight = Math.max(maxDeltaHeight, curr - acc); 
      return curr;   
  }, 0);
  [...verticalCuts, w].reduce((acc, curr) => {
      maxDeltaWidth = Math.max(maxDeltaWidth, curr - acc); 
      return curr;   
  }, 0);
  return BigInt(maxDeltaHeight) * BigInt(maxDeltaWidth) % BigInt(10**9 + 7);
};
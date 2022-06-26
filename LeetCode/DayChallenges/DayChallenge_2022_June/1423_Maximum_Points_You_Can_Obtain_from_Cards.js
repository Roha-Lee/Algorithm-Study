/**
 * @param {number[]} cardPoints
 * @param {number} k
 * @return {number}
 */
 var maxScore = function(cardPoints, k) {
  let minInnerSum = 0;
  let currSum = 0;
  const innerLen = cardPoints.length - k;
  for (let left = 0; left <= k; left += 1) {
      if (minInnerSum === 0) {
          currSum = cardPoints
              .slice(left, left + innerLen)
              .reduce((acc, curr) => acc + curr, 0);
          minInnerSum = currSum;
      }
      else {
          currSum = currSum - cardPoints[left-1] + cardPoints[left + innerLen - 1];
          minInnerSum = Math.min(minInnerSum, currSum);
      }   
  }
  return cardPoints.reduce((acc, curr) => acc + curr, 0) - minInnerSum;
};
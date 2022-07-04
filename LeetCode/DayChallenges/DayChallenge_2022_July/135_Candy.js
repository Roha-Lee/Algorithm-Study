/**
 * @param {number[]} ratings
 * @return {number}
 */
 var candy = function(ratings) {
  const moreForward = new Array(ratings.length).fill(1);
  const moreBackward = new Array(ratings.length).fill(1);
  let candies = 0;
  for (let i = 1; i < ratings.length; i += 1) {
      if (ratings[i] - ratings[i-1] > 0) {
          moreForward[i] = moreForward[i-1] + 1;
      }
  }
  for (let i = ratings.length - 2; i > -1; i -= 1) {
      if (ratings[i] - ratings[i+1] > 0) {
          moreBackward[i] = moreBackward[i+1] + 1;
      }
  }
  for (let i = 0; i < ratings.length; i += 1) {
      candies += Math.max(moreForward[i], moreBackward[i]);
  }
  return candies;
};
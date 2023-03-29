/**
 * @param {number[]} satisfaction
 * @return {number}
 */
var maxSatisfaction = function(satisfaction) {
    satisfaction.sort((a, b) => a - b);
    let index = satisfaction.findIndex((value) => value >= 0);
    if (index === -1) return 0;
    
    let cummulated = satisfaction.reduce((acc, cur) => {
      if (cur >= 0) {
        acc += cur;
      }
      return acc;
    }, 0);
    while (-satisfaction[index] < cummulated) {
      cummulated += satisfaction[index];
      index -= 1;
    }
    return satisfaction.reduce((acc, cur, i) => {
      if (index > i) return acc;
      return acc + cur * (i-index);
    }, 0);
  };

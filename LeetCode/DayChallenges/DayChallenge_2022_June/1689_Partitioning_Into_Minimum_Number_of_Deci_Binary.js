/**
 * @param {string} n
 * @return {number}
 */
 var minPartitions = function(n) {
  let largestNumber = -1;
  for (let digit of n.split("")) {
      largestNumber = Math.max(largestNumber, digit);
  } 
  return largestNumber;
};
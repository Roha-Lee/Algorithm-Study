/**
 * @param {number[][]} people
 * @return {number[][]}
 */
 var reconstructQueue = function(people) {
  people.sort((a, b) => {
      if(a[0] === b[0]) return a[1] > b[1] ? 1 : -1;
      return a[0] < b[0] ? 1 : -1;
  });
  const reconstructed = [];
  for(let [height, front] of people) {
      reconstructed.splice(front, 0, [height, front]);
  }
  return reconstructed;
};
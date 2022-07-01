/**
 * @param {number[][]} boxTypes
 * @param {number} truckSize
 * @return {number}
 */
 var maximumUnits = function(boxTypes, truckSize) {
  let numOfBoxes = 0;
  let num;
  boxTypes.sort((a, b) => a[1] < b[1] ? 1 : -1);
  for (let [box, unit] of boxTypes) {
      if (truckSize === 0) break;
      num = Math.min(box, truckSize);
      truckSize -= num;
      numOfBoxes += num * unit;
  } 
  return numOfBoxes;
};
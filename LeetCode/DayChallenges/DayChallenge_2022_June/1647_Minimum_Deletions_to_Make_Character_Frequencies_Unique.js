/**
 * @param {string} s
 * @return {number}
 */
 var minDeletions = function(s) {
  const counter = new Map();
  const freqCounter = new Map();
  let currFreq = 0;
  let result = 0;
  s.split("").forEach((letter) => {
      counter.set(letter, (counter.get(letter) ?? 0) + 1); 
      currFreq = Math.max(counter.get(letter), currFreq);
  });
  for (let [,freq] of counter) {
      freqCounter.set(
          freq, 
          (freqCounter.get(freq) ?? 0) + 1
      );
  }
  for (;currFreq > 0; currFreq -= 1) {
      let freq = freqCounter.get(currFreq);
      if (freq > 1) {
          result += (freq - 1);
          freqCounter.set(
              currFreq - 1, 
              (freqCounter.get(currFreq - 1) ?? 0) + freq - 1
          );
      }
  }
  return result;
};
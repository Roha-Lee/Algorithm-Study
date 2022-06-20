/**
 * @param {string[]} words
 * @return {number}
 */
 var minimumLengthEncoding = function(words) {
  const suffices = new Set();
  let suffix;
  let length = 0;
  words.sort((a, b) => a.length < b.length ? 1 : -1);
  words.forEach((word) => {
      if (suffices.has(word)) return;
      length += word.length + 1;
      for (let start = 0; start < word.length; start += 1) {
          suffices.add(word.substr(start));
      }
  });
  return length;
};
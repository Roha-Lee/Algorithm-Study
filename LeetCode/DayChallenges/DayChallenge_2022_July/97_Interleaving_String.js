/**
 * @param {string} s1
 * @param {string} s2
 * @param {string} s3
 * @return {boolean}
 */
 var isInterleave = function(s1, s2, s3) {
  let [m, n] = [s1.length, s2.length];
  let temp;
  if (m + n !== s3.length) return false;
  if (n > m) {
      temp = n;
      n = m;
      m = temp;
      temp = s1;
      s1 = s2;
      s2 = temp;
  }
  const dp = new Array(n + 1).fill(false);
  dp[0] = true;
  for (let i = 1; i < n + 1; i += 1) {
      dp[i] = dp[i-1] && s2[i-1] === s3[i-1];
  }
  for (let i = 1; i < m + 1; i += 1) {
      dp[0] = dp[0] && s1[i-1] === s3[i-1];
      for (let j = 1; j < n + 1; j += 1) {
          dp[j] = 
              (s1[i-1] === s3[i+j-1] ? dp[j] : false) ||
              (s2[j-1] === s3[i+j-1] ? dp[j-1]: false);
      }
  }
  return dp[dp.length-1];
};

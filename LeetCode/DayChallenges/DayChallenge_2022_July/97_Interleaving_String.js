/**
 * @param {string} s1
 * @param {string} s2
 * @param {string} s3
 * @return {boolean}
 */
 var isInterleave = function(s1, s2, s3) {
  const [m, n] = [s1.length, s2.length];
  if (m + n !== s3.length) return false;
  const dp = new Array(Math.min(m, n) + 1).fill(false);
  dp[0] = true;
  for (let i = 1; i < Math.min(m, n) + 1; i += 1) {
      dp[i] = dp[i-1] && s2[i-1] === s3[i-1];
  }
  for (let i = 1; i < Math.max(m, n) + 1; i += 1) {
      dp[0] = dp[0] && s1[i-1] === s3[i-1];
      for (let j = 1; j < Math.min(m, n) + 1; j += 1) {
          dp[j] = 
              s1[i-1] === s3[i+j-1] ? dp[j] : false ||
              s2[j-1] === s3[i+j-1] ? dp[j-1]: false;
      }
  }
  return dp[dp.length-1];
};

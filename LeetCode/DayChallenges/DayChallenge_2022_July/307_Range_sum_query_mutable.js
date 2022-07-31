function NumArray(nums) {
    const N = nums.length;
    const dp = Array(N+1).fill(0);
    const vals = Array(N).fill(0);
    for (let i = 0; i < N; i++) {
      update(i, nums[i]);
    }
    
    return { update, sumRange };
    
    function update(i, v) {
      let delta = v - vals[i];
      vals[i] = v;
      for (let idx = i+1; idx <= N; idx += -idx&idx) {
        dp[idx] += delta;
      }
    }
    
    function sumRange(i, j) {
      return getSum(j) - getSum(i-1);
    }
    
    function getSum(i) {
      let sum = 0;
      for (let idx = i + 1; idx >= 1; idx -= -idx&idx) {
        sum += dp[idx];
      }
      
      return sum;
    }  
  }
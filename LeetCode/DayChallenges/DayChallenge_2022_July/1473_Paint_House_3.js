/**
 * @param {number[]} houses
 * @param {number[][]} cost
 * @param {number} m
 * @param {number} n
 * @param {number} target
 * @return {number}
 */
 var minCost = function(houses, cost, m, n, target) {
  let map = new Map();

  function dfs(idx = 0, prevColor = -1, neighborhoods = 0) {
      if (idx === m) return neighborhoods === target ? 0 : Infinity;

      let key = `${idx}-${prevColor}-${neighborhoods}`;
      if (map.has(key)) return map.get(key);
      
      let color = houses[idx];
      if (color > 0) {
          return color !== prevColor ? dfs(idx + 1, color, neighborhoods + 1) : dfs(idx + 1, color, neighborhoods);
      }

      let minCost = Infinity;
      for (let i = 1; i <= n; i++) {
          let potentialCost;
          if (i !== prevColor) potentialCost = dfs(idx + 1, i, neighborhoods + 1);
          else potentialCost = dfs(idx + 1, i, neighborhoods);
          
          if (potentialCost === Infinity) continue;
          minCost = Math.min(minCost, cost[idx][i - 1] + potentialCost);
      }
      map.set(key, minCost);
      return minCost;
  }
  
  let minCost = dfs();
  return minCost === Infinity ? -1 : minCost;
};
# 416. Partition Equal Subset Sum
[문제 링크](https://leetcode.com/problems/partition-equal-subset-sum/)
# 요구 조건 
- 주어진 nums를 합이 같은 두개의 파티션으로 나눌 수 있는지 판단
# 제한 사항 
- `1 <= nums.length <= 200`
- `1 <= nums[i] <= 100`
# 풀이 
1. 주어진 nums의 총합을 2로 나누어서 나누어 떨어지지 않는다면 2개의 파티션으로 나눌 수 없다. 
2. 2로 나눌 수 있다면 각 파티션의 합은 sum(nums) // 2가 되고 이는 0/1 knapsack problem 으로 해결할 수 있다. 
3. 내림차순으로 정렬한 후 큰 숫자(num)부터 DP배열을 아래의 점화식을 이용하여 역순으로 채운다. 
    - `DP[i] = max(DP[i-num] + num, DP[i])`
4. target == DP[-1]를 반환한다. 
# 1200. Minimum Absolute Difference
[문제 링크](https://leetcode.com/problems/minimum-absolute-difference/)
# 요구조건 
- 서로 다른 값을 갖는 arr에서 두 원소의 차의 절대값이 가장 작은 쌍을 모두 구하자.  
# 문제 제한 
- `2 <= arr.length <= 10^5`
- `-10^6 <= arr[i] <= 10^6`
# 풀이
- 가장 차이가 작은 쌍을 찾아야 하므로 정렬을 수행한 후 인접한 원소들끼리만 비교하면 된다. 
- minimum이 갱신되는 경우 list를 새로 생성하고 순서쌍을 넣어준다. 
- minimum이 같은 경우 list에 순서쌍을 넣어준다. 
- minimum보다 큰 경우 아무것도 하지 않고 다음으로 넘어간다. 
# 시간 복잡도
- 정렬 : O(NlogN)
- 인접한 원소들끼리 비교 : O(N)
- 전체 시간복잡도 : O(NlogN)

# 310. Minimum Height Trees
[문제 링크](https://leetcode.com/problems/minimum-height-trees/)
# 요구 조건 
- minimum height tree를 만드는 루트 노드를 리스트로 반환하자. 
# 제한 사항 
- `1 <= n <= 2 * 10^4`
- `edges.length == n - 1`
- `0 <= ai, bi < n`
- `ai != bi`
- 모든 `(ai, bi)`쌍은 서로 다르다. 
- 반복되는 edge는 없다. 
# 풀이 
- topological sort비슷하게 해결하였다. 
- 처음에 leaf노드로 큐를 만들었다.(이웃이 1개인 경우가 leaf노드)
- 현재 노드를 지워가면서 이웃이 1개가 된 경우 새로운 큐에 넣어 다음 큐를 만든다. 
- 더 이상 다음 큐를 만들수 없을 때가 정답이 된다. 
# 시간 복잡도 
- 모든 노드를 한번씩 돌면서(deque-popleft: O(1)) 
- 이웃을 지우고(set을 사용하여 O(1) - 해시충돌이 일어나지 않는다고 가정) 
- 새로운 노드를 추가하는(deque-append: O(1)))
- 따라서 O(V)


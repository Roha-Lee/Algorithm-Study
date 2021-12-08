# 563. Binary Tree Tilt
[문제 링크](https://leetcode.com/problems/binary-tree-tilt/)
# 요구 조건 
- 트리의 tilt의 합을 구하자.
- 각 노드의 tilt란 $|Sum(left sub tree) - Sum(right sub tree)|$를 의미한다. 
# 제한 사항 
- 노드의 개수는 $10^4$이하
# 풀이 
- dfs를 이용하여 해결하였다. 
- 모든 노드를 거쳤다가 돌아갈 때 아래의 두 값을 반환하도록 작성하였다. 
    1. 그 노드를 루트로 하는 서브트리의 노드 합
    2. 그 노드를 루트로 하는 서브트리의 틸트 합
- 리프노드인 경우 `node.val, 0`을 반환
- 노드가 None인 경우 `0 0`을 반환하도록 해주었다. 
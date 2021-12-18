# 938. Range Sum of BST
[문제 링크](https://leetcode.com/problems/range-sum-of-bst/)
# 요구조건 
- low이상 high이하의 모든 수를 tree에서 찾아서 더하라.
# 문제 제한 
- tree의 node개수는 `[1, 2*10^4]`
- `1 <= Node.val <= 10^5`
- `1 <= low <= high <= 10^5`
- 모든 Node.val은 서로 다르다. 
# 풀이
- preorder traversal을 하면서 범위내에 있는 모든 수를 더해주었다. 
# 시간 복잡도
- 모든 tree의 노드를 방문하므로 O(V)

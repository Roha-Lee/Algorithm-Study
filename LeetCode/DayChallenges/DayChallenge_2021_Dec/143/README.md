# 143. Reorder List
[문제 링크](https://leetcode.com/problems/reorder-list/)
# 요구조건 
- `L0, L1, L2, ..., Ln-1, Ln` 순서로 되어있는 연결 리스트를 
- `L0, Ln, L2, Ln-1, ...` 순서로 바꾸자
# 문제 제한 
- `1 <= node의 개수 <= 5 * 10^4`
- `1 <= Node.val <= 1000`
# 풀이
- slow, fast(runner)를 이용하여 연결리스트의 중간 지점을 구한다
- 중간 지점 이후의 연결리스트를 뒤집는다. 
    - 재귀함수를 이용하여 뒤집는다. 
- 뒤집은 연결리스트와 정방향 연결리스트를 이용하여 주어진 조건을 만족하도록 연결해준다. 
# 복잡도
- 시간복잡도
    - 중간 지점 찾기: O(N/2)
    - 연결리스트 뒤집기: O(N)
    - reorder: O(N)
    - 총 시간복잡도: O(N)
- 공간복잡도
    - forward head, reverse head -> O(1)


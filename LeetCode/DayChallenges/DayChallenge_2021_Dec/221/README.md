# 221. Maximal Square
[문제 링크](https://leetcode.com/problems/maximal-square/)
# 요구조건
- 1로 구성된 가장 큰 정사각형의 넓이를 구하자
# 문제 제한 
- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 300`
- `matrix[i][j] is '0' or '1'`
# 풀이
1. Sliding window를 이용한 parametric search풀이 
- `left = 1`, `right = min(m, n)`으로 시작하면서 중간값을 sliding window의 길이로 선택한다. 
- 모든 matrix를 탐색하면서 r, c위치에서의 window크기의 사각형을 탐색하여 하나라도 있는 경우 True를 반환하고 없는 경우 False를 반환한다. 
    - r, c위치에서 window안에 모두 1이 아닌경우 False, 모두 1인 경우 True를 반환한다. 
- 하나라도 정사각형이 있으면 `left = mid + 1`, 없으면 `right = mid - 1`을 넣어서 parametric search를 한다. 
2. DP를 이용한 풀이 
- DP table을 만든다. 이때 각 원소는 (r, c)에서 끝나는 정사각형의 최대 변의 길이를 담도록 한다. 
- `matrix[r][c] == '0'`인 경우는 `DP[r][c]=0`를 넣어주고 `matrix[r][c] == '1'`인 경우는 `DP[r][c] = min(DP[r-1][c], DP[r][c-1], DP[r-1][c-1]) + 1`을 넣어준다. 
- `max_square`를 `DP[r][c] **` 2와 현재 max값을 비교하여 큰 값을 넣어준다. 
- `max_square`를 반환한다. 
# 시간 복잡도
1. sliding window 풀이 
    - `m x n matrix`에서 sliding window를 돌아서 4중 반복문을 돈다.
    - `O((m-window+1) * (n-window+1) * window * window)`의 시간 복잡도
2. DP 풀이 
    - 반복문으로 `m x n`만큼만 값을 갱신하기 때문에 `O(m * n)`
# 1446. Consecutive Characters
[문제 링크](https://leetcode.com/problems/consecutive-characters/)
# 요구조건 
- 스트링의 power는 동일한 글자가 반복되는 최대 substring의 길이로 정의할 수 있다. power를 구하자. 
# 문제 제한 
- `1 <= s.length <= 500`

# 풀이
- 스트링의 두번째 글자부터 맨 마지막까지 탐색하여 `s[i] == s[i-1]`이면 숫자를 늘리고 아니면 최대값을 갱신하고 숫자를 1로 초기화 해준다. 
- 마지막에 현재까지 센 길이와 기존의 최대값 중 최대값을 반환하면 된다. 
# 시간 복잡도
- string의 길이만큼 반복문을 돌기 때문에 O(N)

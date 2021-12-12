# 878. Nth magical number 
[문제 링크](https://leetcode.com/problems/nth-magical-number/)
# 요구 조건 
- a 또는 b로 나누어 떨어지는 수들을 magical number라고 할때 n번째 magical number를 구하자 
# 제한 사항 
- n은 10^9 이하 
- 2 <= a, b <= 4 * 104
- 답이 큰 수가 될 수 있으므로 10^9 + 7로 나눈 나머지를 반환할 것
# 풀이 
- a와 b의 LCM까지 a와 b가 만드는 패턴을 생각해보자
- LCM까지 a는 LCM/a개 b는 LCM/b개의 숫자가 있기 때문에 이를 나열해보면 `{a, 2a, ..., LCM, b, 2b, ..., LCM}`이다. 
    - 마지막 LCM을 제외하고는 중복되는 수가 없다. 
        - 있다면 그게 더 작은 LCM이어야 한다. 
- 마지막 LCM을 제외하고 sort한다. 이때 sort하는 원소의 개수는 `seq_len = LCM/a + LCM/b - 1`개
- n은 n/seq_len만큼 sequence가 반복되므로 몫과 나머지를 구한다. 
    - 0-index이므로 `q = (n-1) // seq_len`, `r = (n-1) % seq_len`
    - 구하려는 값은 `LCM * q + sequence[r]`이 된다. 
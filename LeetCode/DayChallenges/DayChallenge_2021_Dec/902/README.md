# 902. Numbers At Most N Given Digit Set
[문제 링크](https://leetcode.com/problems/numbers-at-most-n-given-digit-set/)
# 요구 조건 
- 오름차순으로 정렬되어있는 digits과 n이 들어왔을때 digits을 이용하여 n이하의 숫자를 만들 수 있는 가짓수를 구하자.
# 제한 사항 
- `1 <= digits.length <= 9`
- `1 <= n <= 10^9`
# 풀이 
- 자리수보다 적은 digit을 이용하여 숫자를 만드는 경우, 자리수만큼의 digit을 이용하여 숫자를 만드는 경우로 나누어서 해결하였다. 
- 자리수보다 적은 digit을 이용하여 숫자를 만드는 경우
    - 모든 digit을 이용할 수 있기 때문에 일의 자리 숫자를 만드는 경우는 `len_digit`, 10의 자리 숫자를 만드는 경우는 `(len_digit)^2`, 10^k자리 숫자를 만드는 경우는 `(len_digit)^(k+1)`만큼의 가짓수가 있다. 이 모든 숫자를 더해준다. 
- 자리수만큼 digit을 이용하여 숫자를 만드는 경우 
    - 예를 들어 digits이 `[1,3,5,7]`이고 `n = 635`인 경우를 생각해보자 
        - 첫번째 자리수를 채우는 방법은 `1, 3, 5`가 있고 나머지 자리수의 경우는 아무 숫자나 오면 되므로 `3 * (len_digit)^2`의 경우의 수가 있다. 
    - 다음으로 digits이 `[1,3,5,7]`이고 `n = 335`인 경우를 생각해보자 
        - 첫번째 자리수를 채우는 방법은 1과 3이 있다. 1을 채우는 경우는 나머지 자리수에 아무 숫자나 오면 된다. 
        - 3을 채우는 경우는 십의자리의 숫자를 고려해야한다. 
    - 나의 풀이에서는 자리수의 숫자 미만의 digits 개수를 `(len_digit)^i`만큼 곱한 후 현재 자리수가 digits에 있는 수라면 다음 자리수로 이동하여 자리수 미만의 digits수와 `(len_digit)^(i-1)`을 곱하는 방식을 계속한다. 
        - 현재 자리수가 digits에 없을 때까지 반복한다. 
    - 마지막자리수의 경우는 다음 자리수가 없으므로 미만이 아니라 이하로 생각하면 된다(특별 처리를 따로 해주었다.)
# 시간복잡도 
- 자리수만큼 반복문: O(log_10(N))
- 특정 digit 미만의 숫자를 세는 로직
    - 선형으로 탐색할 경우 10
    - 이분탐색을 이용하는 경우 log_2(10)
- 전체 시간 복잡도: logN
    

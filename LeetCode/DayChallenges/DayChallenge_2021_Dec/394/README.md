# 394. Decode String
[문제 링크](https://leetcode.com/problems/decode-string/)
# 요구 조건 
- `k[encoded_string]`은 encoded_string을 3번 반복 
- 주어진 encoded string을 decode하자.
# 제한 사항 
- 입력 스트링은 언제나 유효하다 - 공백 없고, 괄호가 잘 구축되어있다.
- `1 <= s.length <= 30`
- s의 모든 정수는 `[1, 300]`에 포함된다. 
# 풀이 
- stack을 이용하여 풀었다. 
- `']'`가 아닌 모든 글자에 대해서는 stack에 넣어준다. 
- `']'`가 등장하게 되면 `'['`가 나올때까지 모든 글자를 앞에 붙여가며 더한다. 
- `'['`를 빼주기 위해 한번 pop한다. 
- 숫자 부분을 얻어내기 위해 isdigit을 이용하여 숫자를 구하고 그 숫자만큼 만들었던 string을 반복해준다. 
- 만든 string을 다음 연산에 사용하기 위해 stack에 넣어준다. 
- stack에 있는 모든 string들을 join을 이용하여 더해준다. 
# 시간 복잡도 
- 모든 글자를 한번씩 stack에 넣고 빼므로 시간 복잡도는 O(N)
# 790. Domino and Tromino Tiling
[문제 링크](https://leetcode.com/problems/domino-and-tromino-tiling/)
# 요구 조건 
- 2 * n 모양의 보드에 도미노와 트로미노를 놓을 수 있는 경우의 수를 구하자 
# 제한 사항 
- n은 1000 이하 
- 답이 큰 수가 될 수 있으므로 10^9 + 7로 나눈 나머지를 반환할 것
# 풀이 
- DP로 풀기 위해 규칙을 찾아보았다. 
![DP 규칙 찾기](https://user-images.githubusercontent.com/82917798/145533578-8527ff09-2b23-4282-8e6d-efbe6bde1a23.jpeg)
- n이 증가할때마다 새로운 패턴이 등장하기 때문에 이를 고려한다면 점화식은 아래와 같다. 
![점화식](https://user-images.githubusercontent.com/82917798/145533813-08161388-26e4-4f54-8c57-6179b8d8f324.jpeg)
- 가로 길이가 1인 패턴을 놓는 경우 나머지는 i-1개를 놓는 경우의 수 -> `DP[i-1]`
- 가로 길이가 2인 패턴을 놓는 경우 나머지는 i-2개를 놓는 경우의 수 -> `DP[i-2]`
- 가로 길이가 k(k>=3)인 패턴은 2개가 있고, 나머지는 i-k이므로 -> `2 * DP[i-k]`
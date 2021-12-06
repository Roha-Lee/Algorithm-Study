# 1217. Minumim cost to move chips to the same position
[문제 링크](https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/)
# 풀이 
- 2칸을 움직이는 것은 비용이 없기 떄문에 모든 2칸 차이 나는 위치의 동전들은 비용 없이 하나로 합치는 것이 가능하다. 
- 홀수번째의 동전과 짝수번째의 동전의 개수를 센 후 둘 중 적은 위치의 동전을 코스트 1씩 사용하면서 옮기면 되므로 `min(odd_pos, even_pos)`가 답이 된다. 

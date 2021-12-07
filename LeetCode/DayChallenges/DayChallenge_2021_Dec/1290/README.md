# 1290. Convert Binary Number in a Linked List to Integer
[문제 링크](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/)
# 문제 제한 
- 링크드 리스트는 비어있지 않음 
- 링크드 리스트의 길이는 30을 넘지 않는다. 
- 링크드 리스트의 각 원소는 {0, 1}
# 풀이 
- 이진법으로 변환하는 방식을 그대로 수행 
- result를 0으로 초기화하고 매 노드를 방문할때마다 2배 해 준 후 노드값을 더해준다. 
- *2보다 <<1이 근소한 차이로 더 빨랐다. 
# 147. Insertion Sort List
[문제 링크](https://leetcode.com/problems/insertion-sort-list/)
# 요구조건 
- 단일 연결리스트에서 insertion sort를 수행하라. 
# 문제 제한 
- `1 <= node의 개수 <= 5000`
- `-5000 <= Node.val <= 5000`
# 풀이
- dummy head를 만들고 다음 노드부터 진짜 노드를 넣어준다. 이를 통해 head를 따로 처리하는 연산을 하지 않아도 된다. 
- dummy head바로 뒤에 첫번째 노드를 넣어주고 curr를 그 다음 노드로 설정하면서 dummy_head의 맨 끝에 `None`을 넣어준다. 
- curr가 들어갈 위치를 dummy head의 처음부터 찾는다. 찾은 위치를 start라고 할때 아래의 그림과 같은 작업을 수행한다. 
![Insert one node](https://user-images.githubusercontent.com/82917798/146648103-bfca74a7-2792-414a-978f-afca9ce5dd06.jpeg)
- dummy head의 다음 노드(진짜 head)를 반환한다 
# 시간 복잡도
- 모든 노드를 한번씩만 방문하고 연결은 O(1)이므로 전체 시간 복잡도는 O(N)이다. 

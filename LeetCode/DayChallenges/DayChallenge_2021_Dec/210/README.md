# 210. Course Schedule 2
:book: [문제 링크](https://leetcode.com/problems/course-schedule-ii/)
# 요구조건 
- prerequisite리스트 [a, b]는 a를 듣기 위해서는 b를 먼저 들어야 한다는 의미를 갖는다. 
- prerequisites가 주어졌을때 수업을 들어야 하는 순서를 반환하자. 불가능할 경우 빈 리스트를 반환하자. 
# 문제 제한 
- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= numCourses * (numCourses - 1)`
- `prerequisites[i].length == 2`
- `0 <= ai, bi < numCourses`
- `ai != bi`
- 모든 `[ai, bi]`는 서로 다르다. 
# 풀이
- topological sort를 이용하여 풀었다. 
- prev_course의 neighbor로 next_course를 넣어서 커리큘럼 그래프를 만들었다. 
- inward count가 0인 노드들을 큐에 넣고 큐를 돌면서 큐에서 하나를 빼서 result에 넣고 그 노드의 neighbor의 inward count를 1씩 감소시키면서 다시 0이 된 노드들을 큐에 넣는 작업을 반복한다. 
- result의 길이가 전체 코스의 길이와 동일하면 정상적으로 topological sort가 완료된 것이므로 result를 반환한다. 
- 아닌 경우 빈 리스트를 반환한다. 
# 시간 복잡도
- topological sort에서 큐에 모든 노드가 한번씩 들어갔다 나오고 각 노드에서 이웃을 방문할때 모든 간선을 방문하기 때문에 O(|E| + |V|)
import sys 
from collections import deque
input = sys.stdin.readline
testcase_num = int(input())

for _ in range(testcase_num):
    priority = 1
    doc_num, query = map(int, input().split())
    doc_indices = deque(range(doc_num))
    scores = deque(map(int, input().split()))
    while scores:
        max_score = max(scores)
        curr_score = scores.popleft()
        curr_doc = doc_indices.popleft()
        while not max_score == curr_score:
            doc_indices.append(curr_doc)
            scores.append(curr_score)
            curr_score = scores.popleft()
            curr_doc = doc_indices.popleft()
        if query == curr_doc:
            print(priority)
            break
        priority += 1    
        
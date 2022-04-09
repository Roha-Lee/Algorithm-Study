from collections import Counter

def combinations(order, idx, result, temp = []):
    if len(order) == idx:
        return 
    for i in range(idx, len(order)):
        temp.append(order[i])
        if len(temp) > 1:
            result.append(''.join(temp))
        combinations(order, i+1, result, temp)
        temp.pop()
    return 
    
def solution(orders, course):
    answer = []
    max_len = 0
    for order in orders:
        max_len = max(max_len, len(order))
    course_dict = {i:Counter() for i in range(2, max_len + 1)}
    
    for order in orders:
        result = []
        order = sorted(list(order))
        combinations(order, 0, result)
        for combination in result:
            if len(combination) > 1:
                course_dict[len(combination)][combination] += 1
    
    for num in course:
        if num in course_dict:
            max_num = course_dict[num].most_common(1)[0][1] 
            if max_num > 1:
                answer.extend([item for item in course_dict[num] if course_dict[num][item] == max_num])
    
    return sorted(answer)
        
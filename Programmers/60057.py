def compression(s, num):
    result = ''
    prev = ''
    count = 1
    for i in range(0, len(s), num):
        curr = s[i:i+num]
        if prev == curr:
            count += 1
        else:
            if count == 1:
                result += prev
            else:
                result += '%d%s'%(count, prev)
            count = 1
            prev = curr
    if count == 1:
        result += prev
    else:
        result += '%d%s'%(count, prev)

    return result


def solution(s):
    if len(s) == 1:
        return 1
    answer = float('inf')
    for num in range(1, len(s) // 2 + 1):
        answer = min(answer, len(compression(s, num)))
    return answer
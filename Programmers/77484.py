def solution(lottos, win_nums):
    unknown = lottos.count(0)
    count = len([num for num in lottos if num in win_nums])
    return [min(6, 7-unknown-count), min(6, 7-count)]
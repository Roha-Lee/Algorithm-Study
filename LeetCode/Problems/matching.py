from itertools import combinations
import random
def matching(rounds, num_groups, game_per_round):
    result = []
    used_combinations = set()
    candidates = [(groupA, groupB) for groupA, groupB in combinations(range(1, num_groups+1), 2)]
    for round in range(rounds):
        random.shuffle(candidates)
        used_group = set()
        matching = []
        for (groupA, groupB) in candidates:
            if groupA > groupB:
                groupA, groupB = groupB, groupA
            if groupA in used_group or groupB in used_group or (groupA, groupB) in used_combinations:
                continue
            matching.append((groupA, groupB))
            used_combinations.add((groupA, groupB))
            used_group.add(groupA)
            used_group.add(groupB)
            if len(matching) >= game_per_round:
                break
        result.append((round + 1, matching))
    return result
            
    
    
    
if __name__ == "__main__":
    num_groups = 8
    game_per_round = 5
    rounds = 5
    print(matching(rounds, num_groups, game_per_round))
    
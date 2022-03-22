def rotate(key):
    row, col = len(key), len(key[0])
    rotate_key = [[0] * col for _ in range(row)]
    for r in range(row):
        for c in range(col):
            rotate_key[r][c] = key[c][row-1-r]
    return rotate_key

def canOpen(key, need_key, dr, dc, num_lock):
    key_row, key_col = len(key), len(key[0])
    lock_row, lock_col = len(need_key), len(need_key[0])
    add = 0
    for r in range(key_row):
        for c in range(key_col):
            nr, nc = r + dr, c + dc
            if not(0 <= nr < lock_row and 0 <= nc < lock_col):
                continue
            if key[r][c] == 1 and need_key[nr][nc] == 0:
                return False
            add += 1 if key[r][c] == 1 and need_key[nr][nc] == 1 else 0
    return add == num_lock
            
def solution(key, lock):
    num_key, num_lock = 0, 0
    need_key = [[0] * len(lock[0]) for _ in range(len(lock))]
    key_row, key_col = len(key), len(key[0])
    lock_row, lock_col = len(lock), len(lock[0])
    for i in range(key_row):
        for j in range(key_col):
            num_key += key[i][j]
    for i in range(lock_row):
        for j in range(lock_col):
            need_key[i][j] = 1 - lock[i][j]
            num_lock += need_key[i][j]
            
    if num_key < num_lock:
        return False
    
    # sliding window
    curr_key = key
    for _ in range(4):
        curr_key = rotate(curr_key)
        for dr in range(-key_row + 1, lock_row):
            for dc in range(-key_col + 1, lock_col):
                if canOpen(curr_key, need_key, dr, dc, num_lock):
                    return True
    return False
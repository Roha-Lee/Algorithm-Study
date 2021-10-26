import sys 

def dfs(length, letter = '', loc = 0, num_vowel = 0):
    if len(letter) == length and 0 < num_vowel < length - 1:
        print(letter)
        return 
    for i in range(loc, c):
        dfs(length, letter+letters[i], i + 1, num_vowel + (letters[i] in vowel))
# 1개의 모음 2개의 자음     
if __name__ == "__main__":
    vowel = ['a','i','e','o','u']
    input = sys.stdin.readline
    l, c = map(int, input().split())
    letters = sorted(input().split())
    dfs(l)
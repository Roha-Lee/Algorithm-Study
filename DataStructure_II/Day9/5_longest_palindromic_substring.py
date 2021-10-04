# Manacher Algorithm 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        aug_s = '#' + '#'.join(list(s)) + '#'
        N = len(aug_s)
        A = [0 for _ in range(N)]
        max_loc = 0
        for i in range(1, N):
            r, p = 0, 0
            if i <= r:
                A[i] = min(r-i, A[2*p-i])

            while i - A[i] >= 0 and i + A[i] < N and aug_s[i - A[i]] == aug_s[i + A[i]]:
                A[i] += 1
            A[i] -= 1
            if A[i] + i > r:
                r = i + A[i]
                p = i

            if A[max_loc] < A[i]:
                max_loc = i


        if max_loc % 2 == 0:
            win = int((A[max_loc]) / 2) 
            max_loc = int((max_loc - 1) / 2)
            return s[max_loc-win+1:max_loc+win+1]
        else:
            win = int((A[max_loc] - 1) / 2)
            max_loc = int((max_loc - 1) / 2)    
            return s[max_loc-win: max_loc+win+1]

# def longestPalindrome(s):
#     aug_s = '#' + '#'.join(list(s)) + '#'
#     N = len(aug_s)
#     A = [0 for _ in range(N)]
#     max_loc = 0
#     for i in range(1, N):
#         r, p = 0, 0
#         if i <= r:
#             A[i] = min(r-i, A[2*p-i])
            
#         while i - A[i] >= 0 and i + A[i] < N and aug_s[i - A[i]] == aug_s[i + A[i]]:
#             A[i] += 1
#         A[i] -= 1
#         if A[i] + i > r:
#             r = i + A[i]
#             p = i
        
#         if A[max_loc] < A[i]:
#             max_loc = i
    
    
#     if max_loc % 2 == 0:
#         win = int((A[max_loc]) / 2) 
#         max_loc = int((max_loc - 1) / 2)
#         return s[max_loc-win+1:max_loc+win+1]
#     else:
#         win = int((A[max_loc] - 1) / 2)
#         max_loc = int((max_loc - 1) / 2)    
#         return s[max_loc-win: max_loc+win+1]

    
        


# # # 파이썬이 느리긴 한가보다 같은 코드여도 통과할 때 있고 안될때가 있네.. 나름 최적화 한다고 한건데 
# # class Solution:
# #     @functools.lru_cache(maxsize=None)
# #     def longestPalindrome(self, s: str) -> str:
# #         DP_mtx = [[False for _ in range(len(s))] for _ in range(len(s))]
# #         loc_i = 0
# #         loc_j = 0
# #         for d in range(len(s)):
# #             skip = d < 2
# #             for c in range(d, len(s)):
# #                 r = c - d
# #                 if skip or DP_mtx[r+1][c-1]:
# #                     DP_mtx[r][c] = s[r] == s[c]
# #                     if DP_mtx[r][c] and loc_j - loc_i < d:
# #                         loc_i = r
# #                         loc_j = c
# #                 else:
# #                     DP_mtx[r][c] = False
# #         return s[loc_i:loc_j+1]

# # # # Slow 
# # # def longestPalindrome(s):
# # #     rows = 2
# # #     cols = len(s)
# # #     iters = int(len(s)//2 + 1)
# # #     DP_mtx = [[0 for _ in range(cols)] for _ in range(rows)]
# # #     max_win = 1
# # #     for _ in range(iters):
# # #         for c in range(cols):
# # #             odd_win = DP_mtx[0][c] + 1
# # #             if max_win > odd_win:
# # #                 continue
# # #             if not(c-odd_win < 0 or c+odd_win>=cols):    
# # #                 if s[c-odd_win] == s[c+odd_win]:
# # #                     DP_mtx[0][c] = odd_win
# # #             even_win = DP_mtx[1][c] + 1
# # #             if max_win > even_win:
# # #                 continue
# # #             if not(c-even_win+1 < 0 or c+even_win>=cols):
# # #                 if s[c-even_win+1] == s[c+even_win]:
# # #                     DP_mtx[1][c] = even_win
    
# # #     max_odd = max(DP_mtx[0])
# # #     max_even = max(DP_mtx[1])
# # #     max_idx = -1
# # #     is_odd = False
# # #     if max_odd < max_even:
# # #         for i in range(len(DP_mtx[1])):
# # #             if DP_mtx[1][i] == max_even:
# # #                 max_idx = i
# # #                 is_odd = False
# # #                 break
# # #     else:
# # #         for i in range(len(DP_mtx[0])):
# # #             if DP_mtx[0][i] == max_odd:
# # #                 max_idx = i
# # #                 is_odd = True
# # #                 break
# # #     if is_odd:
# # #         return s[ max_idx-max_odd : max_idx+max_odd+1 ]
# # #     else:
# # #         return s[ max_idx-max_even+1 : max_idx+max_even+1 ]

# # def longestPalindrome(s):
# #     DP_mtx = [[False for _ in range(len(s))] for _ in range(len(s))]
# #     loc_i = 0
# #     loc_j = 0
# #     for d in range(len(s)):
# #         for c in range(d, len(s)):
# #             r = c - d
# #             if d < 2 or DP_mtx[r+1][c-1]:
# #                 DP_mtx[r][c] = s[r] == s[c]
# #                 if DP_mtx[r][c] and loc_j - loc_i < d:
# #                     loc_i = r
# #                     loc_j = c
# #             else:
# #                 DP_mtx[r][c] = False
# #     return s[loc_i:loc_j+1]

# if __name__ == '__main__':
#     inputs = ['babad','cbbd','a','ac','bb']
#     outputs = [['bab', 'aba'], ['bb'], ['a'], ['a','c'], ['bb']]
    
#     def test(fn, inputs, outputs):
#         for (i, out) in zip(inputs, outputs):
#             if fn(i) in out:
#                 print('Correct!')
#             else:
#                 print('Incorrect!')

#     test(longestPalindrome, inputs, outputs)

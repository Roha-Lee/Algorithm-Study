from pprint import pprint
def longestCommonSubsequence(text1, text2):
    len1 = len(text1)
    len2 = len(text2)

    if len1 < len2:
        text1, text2 = text2, text1
        len1, len2 = len2, len1
    
    DP_mtx = [[0 for _ in range(len1+1)] for _ in range(len2+1)]
    for i in range(1, len2+1):
        for j in range(1, len1+1):
            if text1[j-1] == text2[i-1]:
                DP_mtx[i][j] = DP_mtx[i-1][j-1] + 1
            else:
                DP_mtx[i][j] = max(DP_mtx[i-1][j], DP_mtx[i][j-1])
    return DP_mtx[-1][-1]

if __name__ == '__main__':
    def test(in1_list, in2_list, ans_list, func):
        for in1, in2, ans in zip(in1_list, in2_list, ans_list):
            print(in1, in2)
            my_ans = func(in1, in2)
            print(my_ans == ans, my_ans, ans)

    test(['abcba', 'abcbcba','oxcpqrsvwf', 'bsbininm', 'psnw', 'vozsh'], 
        ['abcbcba', 'abcba','shmtulqrypy', 'jmjkbkjkv', 'vozsh', 'psnwsh'],
        [5,5,2,1,1,2], 
        longestCommonSubsequence)
            


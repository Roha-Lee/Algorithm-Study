def count_palindrome(s):
    count = len(s)
    for i in range(len(s)):
        for width in range(len(s) - i):
            if (not (i - width < 0 or i + width + 1 >= len(s))) and s[i-width] == s[i+width+1]:
                count += 1
            else:
                break
        for width in range(len(s) - i):
            if (not (i - width - 1 < 0 or i + width + 1 >= len(s))) and s[i-width-1] == s[i+width+1]:
                count += 1
            else:
                break
    return count

print(count_palindrome('abcbaabaabcba'))
print(count_palindrome('aaa'))
print(count_palindrome(''))
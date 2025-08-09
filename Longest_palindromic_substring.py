Input = "babad"

def longest_palindrome(s):
    if len(s) < 1:
        return s
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    max = s[0]

    for i in range(len(s)):
        odd = expand(i, i) #1 3 5 length
    
        even = expand(i, i + 1)#0 2 4 length

        if len(odd) > len(max):
            max = odd
        if len(even) > len(max):
            max = even
    return max

print(longest_palindrome(Input))
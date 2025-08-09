#Given a string s, find the length of the longest substring without duplicate characters.
from collections import deque

Input = "abcabcbb"


def length_of_longest_substring(s):
    res = 0
    q = deque()
    for c in s:
        while c in q:
            while q.popleft() != c:
                pass
        q.append(c)
        res = max(res, len(q))
    return res

print(length_of_longest_substring(Input))
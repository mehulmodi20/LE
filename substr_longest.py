def lengthOfLongestSubstring(s: str) -> int:
    substr = ""
    substr_len = 0
    if len(s) <= 1:
        return len(s)
    for i in range(len(s)):
        if s[i] not in substr:
            substr += s[i]
        else:
            index = substr.index(s[i])
            substr = substr[index + 1 :] + s[i]
        substr_len = max(substr_len, len(substr))
    return substr_len


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("au"))
print(lengthOfLongestSubstring("dvdf"))

#!/usr/bin/env python3

# Source: https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1685103/Python-Sliding-window-%2B-Hashmap-Solution

import sys


def lengthOfLongestSubstring(s: str) -> int:

    window_start = 0
    substring_length = 0
    max_length = 0
    lookup = {}
    for window_end in range(len(s)):

        char = s[window_end]
        print(char)

        # if character in map and character within the current window
        if char in lookup and lookup[char] >= window_start:
            print(lookup[char], window_start)
            # start new window at next position
            print("found b")
            window_start = lookup[char]+1
            # shrink substring length
            substring_length = window_end - window_start
            # print(substring_length)

        lookup[char] = window_end

        print(lookup)
        substring_length += 1
        print(substring_length)
        max_length = max(max_length, substring_length)
    return max_length


if __name__ == '__main__':
    string = sys.argv[1]
    print("Result is ", lengthOfLongestSubstring(string))


# Sample values to test: abcabcbb, dvdf , " ", bbbbb, abba

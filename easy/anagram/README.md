# Description
This program determines the minimum number of character changes required to make the two halves of a string anagrams of each other.
If the string has an odd length, it’s impossible to split it into two equal halves, and the function returns -1.
# Problem Statement
Given a string s, split it into two equal halves.
Determine the minimum number of character changes needed in the first half to make it an anagram of the second half.
If s has odd length, return -1.
Only substitutions are allowed, not insertions or deletions.
Example:
Input: "aaabbb"
Output: 3
Explanation:
First half: "aaa"
Second half: "bbb"
Need to change all 3 'a's in the first half to 'b's.

def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
        
    return max_length

#we are defining a set and using sliding window taking the max valid window into consideration
#below is the one that I wrote

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        n=len(s)
        i=0
        j=0
        st = set()
        while(i<n and j<n):
            if(s[j] not in st):
                ans = max(ans,j-i+1)
                st.add(s[j])
                j += 1
            else:
                st.remove(s[i])
                i += 1
        return ans

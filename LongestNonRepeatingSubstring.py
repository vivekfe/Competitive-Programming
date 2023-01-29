class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        maxl=0
        unique=set()
        for r in range(len(s)):
            while s[r] in unique:
                unique.remove(s[left])
                left=left+1
            unique.add(s[r])
            maxl=max(maxl, r-left+1)
            
        return maxl
      
instance = Solution()
s="abcabcbb"
print(instance.lengthOfLongestSubstring(s))

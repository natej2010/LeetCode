class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        s_len = len(s)
        
        
        if s == s[::-1] or len(s) <= 1:
            return s
        else:
            longest = s[0]
        
        for i in range(1, s_len):
            start = i
            end = i
            
            # Odd
            while start >= 0 and end <= s_len -1:
                if s[start] == s[end]:
                    longest = max(longest, s[start:end+1], key=len)
                    start -= 1
                    end += 1
                else:
                    break
            
            
        for i in range(0, s_len):
            # Even
            start = i
            end = start + 1
            
            while start >= 0 and end <= s_len - 1:
                if s[start] == s[end]:
                    longest = max(longest, s[start:end+1], key=len)
                    start -= 1
                    end += 1
                else:
                    break
        
        return longest

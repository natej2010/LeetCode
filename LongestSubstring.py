class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_sub_string = 0
        sub_string_len = 0
        sub_str = {}
        i = 0
        
        
        while i < len(s):
            
            if s[i] in sub_str:
                if sub_string_len > longest_sub_string:
                    longest_sub_string = sub_string_len
                                
                sub_string_len = 0
                go_back_i = sub_str[s[i]]
                sub_str = {}
                i = go_back_i + 1
                    
            else:
                sub_string_len += 1
                sub_str[s[i]]= i
                i += 1
                
            
         
        if sub_string_len > longest_sub_string:
                    longest_sub_string = sub_string_len
                
        return longest_sub_string
                
                
                
            

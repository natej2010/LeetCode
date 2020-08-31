class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        negative = 1
        result = ""
        
        if not s:
            return 0
        
        if s[0] == '-':
            negative = -1
        elif s[0] == '+':
            negative = 1
        elif not s[0].isdigit():
            return 0
        else:
            result += s[0]
        
        
        for c in s[1:]:
            if c.isdigit():
                result += c
            else:
                break
        try:
            result_int = int(result) * negative
            if result_int > 2**31 - 1:
                return 2**31 - 1
            elif result_int < -2**31:
                return -2**31
            else:
                return result_int
        except:
            return 0

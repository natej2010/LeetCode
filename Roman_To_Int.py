class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }
        
        result = 0
        i = 0
        
        while i < len(s):
            if s[i] == 'C' and i + 1 < len(s) and s[i+1] == 'M':
                result += roman_num['CM']
                i += 1
            elif s[i] == 'C' and i + 1 < len(s) and s[i+1] == 'D':
                result += roman_num['CD']
                i += 1
            elif s[i] == 'X' and i + 1 < len(s) and s[i+1] == 'C':
                result += roman_num['XC']
                i += 1
            elif s[i] == 'X' and i + 1 < len(s) and s[i+1] == 'L':
                result += roman_num['XL']
                i += 1
            elif s[i] == 'I' and i + 1 < len(s) and s[i+1] == 'X':
                result += roman_num['IX']
                i += 1
            elif s[i] == 'I' and i + 1 < len(s) and s[i+1] == 'V':
                result += roman_num['IV']
                i += 1
            else:
                result += roman_num[s[i]]
            
            i += 1
            
        return result

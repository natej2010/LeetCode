class Solution:
    def intToRoman(self, num: int) -> str:
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
        
        remainder = num
        result = ''
        
        for num in sorted(roman_num.items(), key=lambda x:x[1], reverse=True):
            if (ans := remainder // num[1]):
                result = result + num[0] * ans
                remainder = remainder % num[1]
        
        return result
                

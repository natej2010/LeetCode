class Solution:
    def isValid(self, s: str) -> bool:
        brackets = list()
        
        for c in s:
            if c in ['(', '{', '[']:
                brackets.append(c)
            elif c == ')' and brackets:
                if brackets.pop() == '(':
                    continue
                else:
                    return False
            elif c == '}' and brackets:
                if brackets.pop() == '{':
                    continue
                else:
                    return False
            elif c == ']' and brackets:
                if brackets.pop() == '[':
                    continue
                else:
                    return False
            else:
                return False
        if brackets:
            return False
        else:
            return True
            

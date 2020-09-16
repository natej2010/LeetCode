class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        letters = {}
        shortest_word = len(strs[0])
        prefix = ''
        
        for word in strs:
            shortest_word = min(shortest_word, len(word))
            for index, character in enumerate(word):
                if index in letters.keys():
                    letters[index].update(character)
                else:
                    letters[index] = set(character)
        
        for i in range(shortest_word):
  
            if len(letters[i]) == 1:
                prefix = prefix + list(letters[i])[0]
            else:
                break
                
        return prefix

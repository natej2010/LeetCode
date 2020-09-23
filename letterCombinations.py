def build_tree(tree, letters):
    if tree:
        for k, v in tree.items():
            tree[k] = build_tree(v, letters)
    else:
        tree = {}
        for letter in letters:
            tree[letter] = None
            
    return tree

def walk_tree(tree, path):
    paths = []
    
    for k, v in tree.items():
        if v:
            paths += walk_tree(v, path+k)
        else:
            paths.append(path+k)
     
    return paths

class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        keys = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z'],
        }
        
        tree = {}
        
        for digit in digits:
            tree = build_tree(tree, keys[digit])
        
        result = walk_tree(tree, '')
        return result

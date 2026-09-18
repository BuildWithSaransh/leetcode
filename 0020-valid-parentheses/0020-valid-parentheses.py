class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_map = {")": "(","}": "{", "]": "["}
        stack = []
        
        for char in s:
            if char in bracket_map: 
                if not stack or stack[-1] != bracket_map[char]:
                 return  False
                stack.pop()
            else:
               stack.append(char)
        return len(stack) == 0

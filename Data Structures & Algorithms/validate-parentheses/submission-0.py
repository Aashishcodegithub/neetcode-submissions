class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]#list
        OpenToClose={")":"(","}":"{","]":"["}
        for i in s:
            if i in OpenToClose.values():
                stack.append(i)
            elif i in OpenToClose.keys():
                if not stack or OpenToClose[i]!=stack.pop():
                    return False
        return len(stack)==0
                

        
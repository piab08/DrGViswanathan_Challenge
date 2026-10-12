class Solution:
    def isValid(self, s):
        stack = []

        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False

                x = stack.pop()

                if i == ')' and x != '(':
                    return False
                if i == '}' and x != '{':
                    return False
                if i == ']' and x != '[':
                    return False

        return len(stack) == 0
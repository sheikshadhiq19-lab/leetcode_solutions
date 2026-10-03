class Solution(object):
    def backspaceCompare(self, s, t):
        stack1=[]
        stack2=[]
        for ch in s:
            if stack1 and ch=="#":
                stack1.pop()
            elif not stack1 and ch=="#":
                stack1=[]
            else:
                stack1.append(ch)
        for ch in t:
            if stack2 and ch=="#":
                stack2.pop()
            elif not stack2 and ch=="#":
                stack2=[]
            else:
                stack2.append(ch)
        return stack1==stack2
        
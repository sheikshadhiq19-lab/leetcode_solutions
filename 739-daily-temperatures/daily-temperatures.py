class Solution(object):
    def dailyTemperatures(self, temperatures):
        ans=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                index=stack.pop()
                ans[index]=i-index
            stack.append(i)
        return(ans)
        
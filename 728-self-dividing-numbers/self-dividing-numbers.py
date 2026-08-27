class Solution(object):
    def selfDividingNumbers(self, left, right):
        a=[]
        while left<=right:
            l1=list(str(left))
            c=0
            for i in range(len(l1)):
                if l1[i]!='0' and left % int(l1[i])==0:
                    c=c+1
            if c==len(l1):
                a.append(left)
            left=left+1
        return a
         
class Solution(object):
    def isHappy(self, n):
        if n==1:
            return True
        c=0
        while n>0:
            l=list(str(n))
            s=0
            for i in range(len(l)):
                s=s+int(l[i])*int(l[i])
            if s==1:
                return True
            elif c==9:
                return False
            else:
                n=s
                c+=1
        
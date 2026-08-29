class Solution(object):
    def reverseOnlyLetters(self, s):
        l=0
        r=len(s)-1
        char=list(s)
        while l<r:
            if not char[l].isalpha():
                l+=1
            elif not char[r].isalpha():
                r-=1
            else:
                char[l],char[r]=char[r],char[l]
                l+=1
                r-=1
        return "".join(char)
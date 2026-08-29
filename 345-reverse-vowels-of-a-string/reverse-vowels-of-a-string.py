class Solution(object):
    def reverseVowels(self, s):
        v = "aeiouAEIOU"
        l=0
        r=len(s)-1
        char=list(s)
        while l<r:
            while l<r and char[l] not in v:
                l+=1
            while l<r and char[r] not in v:
                r-=1
            char[l],char[r]=char[r],char[l]
            l+=1
            r-=1
        return "".join(char)

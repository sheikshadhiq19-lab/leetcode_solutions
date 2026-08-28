class Solution(object):
    def searchMatrix(self, matrix, target):
        m=len(matrix)
        n=len(matrix[0])
        l=0
        r=(m*n)-1
        while l<=r:
            mid=(l+r)//2
            col=mid//n
            row=mid%n
            if matrix[col][row]==target:
                return True
            elif matrix[col][row]<target:
                l=mid+1
            else:
                r=mid-1
        return False
        
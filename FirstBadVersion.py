def isBadVersion(version):
    if(version>= first_bad):
        return true
    else:
        return false

class Solution:
    def firstBadVersion(self, n):
        if n<2:
            return n
        s=1
        e=n
        while(s<=e):
            mid = (s+e)//2
            if isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            elif isBadVersion(mid-1):
                e=mid-1
            else:
                s=mid+1


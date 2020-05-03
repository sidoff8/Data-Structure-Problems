class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>len(magazine):
            return False
        d={}
        for i in magazine:
            if i in d:
                d[i]+=1
            else:
                d[i]=0
        for c in ransomNote:
            if c not in d:
                return False
            elif d[c]<0:
                return False
            else:
                d[c]-=1
        return True

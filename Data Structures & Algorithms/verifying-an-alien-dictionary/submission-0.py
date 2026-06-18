class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mp={}
        for i in range(26):
            mp[order[i]]=i
        l=0
        while l<len(words)-1:
            r=0
            while r<len(words[l]) and r<len(words[l+1]):
                if words[l][r]!=words[l+1][r]:
                    if mp[words[l][r]]>mp[words[l+1][r]]:
                        return False
                    else:
                        break
                r+=1
            if r==len(words[l+1]):
                return False
            l+=1
        
        return True



        
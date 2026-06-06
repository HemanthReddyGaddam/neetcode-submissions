class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,0
        n=len(numbers)
        ans=[]
        while l<n:
            r=l
            while r<n:
                if numbers[l]+numbers[r]==target:
                    ans.append(l+1)
                    ans.append(r+1)
                    return ans
                elif numbers[l]+numbers[r]>target:
                    break
                else:
                    r+=1
            l+=1
        return ans
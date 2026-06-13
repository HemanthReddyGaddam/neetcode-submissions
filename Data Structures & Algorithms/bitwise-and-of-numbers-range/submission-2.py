class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        sum=0
        n=1
        while n<=left:
            n=n*2
        n=n//2
        sum=n
        if right<2*n:
            while n:
                temp=n//2
                if temp+sum<=left and sum+2*temp>right:
                    sum+=temp
                n=n//2
        else: 
            return 0
        return sum
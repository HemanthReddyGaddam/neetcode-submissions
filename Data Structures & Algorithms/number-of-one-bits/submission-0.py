class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n:
            temp=n%2
            count+=temp
            n=n//2
        return count
        
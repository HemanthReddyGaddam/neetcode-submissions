class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=""
        carry=0

        a,b=a[::-1],b[::-1]
        for i in range(max(len(a),len(b))):
            digitA=ord(a[i])-ord("0") if i<len(a) else 0
            digitB=ord(b[i])-ord("0") if i<len(b) else 0

            curr=digitA+digitB+carry
            res=str(curr%2)+res
            carry=curr//2

        if carry==1:
            res='1'+res
        return res

        
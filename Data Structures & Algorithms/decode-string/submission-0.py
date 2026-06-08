class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]


        for ch in s:
            if ch==']':
                temp=""
                while stack[-1]!='[':
                    temp=stack.pop()+temp
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                val = int(num)
                st=""
                while val>0:
                    st+=temp
                    val-=1
                stack.append(st)
                continue
            stack.append(ch)

        
        return "".join(stack)
        
                



        
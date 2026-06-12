class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]

        def parent(temp,stack):
            if len(temp)==2*n and len(stack)==0:
                ans.append(temp)
                return

            if len(temp)==2*n and len(stack)!=0:
                return

            elif len(stack)==0:
                temp+='('
                stack.append('(')
                parent(temp,stack)
                temp=temp[:-1]
                stack.pop()

            elif stack[-1]=='(':
                temp+='('
                stack.append('(')
                parent(temp,stack)
                temp=temp[:-1]
                stack.pop()
                temp+=')'
                stack.pop()
                parent(temp,stack)
                temp=temp[:-1]
                stack.append('(') 

        parent('',[])

        return ans
            

            
                
        
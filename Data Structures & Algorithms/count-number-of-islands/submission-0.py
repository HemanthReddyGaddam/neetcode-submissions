class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count1=0;
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    count1+=1
        count=0
        num=0
        
        visit=set()
        def dfs(i,j):
            nonlocal count
            if i==len(grid) or j==len(grid[0]) or i<0 or j<0:
                return 
            if (i,j) in visit:
                return
            if grid[i][j]=="0":
                visit.add((i,j))
                return


            else:
                visit.add((i,j))
                count+=1
                dfs(i,j+1)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i-1,j)
                return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visit:
                    num+=1
                    dfs(i,j)
        return num
        

            


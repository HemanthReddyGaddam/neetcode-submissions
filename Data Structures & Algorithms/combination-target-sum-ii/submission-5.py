class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def dfs(curr_sum, ind, temp):
            if curr_sum == target:
                ans.append(temp.copy())
                return
            
            if curr_sum > target or ind==len(candidates):
                return

            temp.append(candidates[ind])
            dfs(curr_sum + candidates[ind], ind+1, temp)
            temp.pop()

            while ind+1<len(candidates) and candidates[ind]==candidates[ind+1]:
                ind+=1
            dfs(curr_sum, ind+1, temp)

        dfs(0, 0, [])
        return ans
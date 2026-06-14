class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans=[]
        def f(x)->int:
            return math.sqrt(x[0]**2 + x[1]**2)

        heap=[(f(x),x) for x in points]
        heapq.heapify(heap)
        for _ in range(k):
            temp=heapq.heappop(heap)
            ans.append(temp[1])

        return ans

        
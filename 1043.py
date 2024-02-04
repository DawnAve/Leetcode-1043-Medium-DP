class Solution:
    # Code from MindOfshridhar
    
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)

        # This is a recursion, also a kind of brute force solution
        def dfs(i):

            # Base case, when we reached the end of the list
            if i == n:
                return 0

            # Reset maxes
            curSum = curMax = 0

            # Loop through subarrays with length k
            for j in range(i, min(i+k,n)):
                curMax = max(curMax, arr[j])

                # In the loop, we cut arrays at all possible places
                # And do dfs to the following array
                """
分区[1]：

最大值为1，只有一个元素，所以当前分区的值为1*1=1。
递归调用dfs(1)，处理数组的剩余部分[15,7,9,2,5,10]。
分区[1, 15]：

最大值为15，分区长度为2，所以当前分区的值为15*2=30。
递归调用dfs(2)，处理数组的剩余部分[7,9,2,5,10]。
分区[1, 15, 7]：

最大值为15，分区长度为3，所以当前分区的值为15*3=45。
递归调用dfs(3)，处理数组的剩余部分[9,2,5,10]。
                """
                cur = curMax * (j-i+1)+dfs(j+1)

                curSum = max(curSum, cur)
            return curSum
        return dfs(0)

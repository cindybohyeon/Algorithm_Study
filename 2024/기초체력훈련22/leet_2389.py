class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # (!) 그리디 풀이
        nums.sort() # 1 2 4 5
        result = []
        n = len(nums)
        # totalSum = sum(nums)

        # for q in queries:
        #     tempResult = 0
        #     tempSum = totalSum
        #     for i in range(n-1, -1, -1):
        #         if tempSum == q:
        #             tempResult = max(i + 1, tempResult)
        #         elif tempSum > q:
        #             tempSum -= nums[i]
        #         else:
        #             tempResult = max(i + 1, tempResult)

        #     result.append(tempResult)

        # return result


        # (2) dp + 이분탐색 upper bound
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = dp[i - 1] + nums[i]
        # print(dp,"dp")
        for q in queries:
            start = 0
            end = n - 1
            temp = n
            while(start <= end):
                mid = (start + end) // 2
                if dp[mid] <= q:
                    start = mid + 1
                else:
                    end = mid - 1    
            temp = start


                    # if mid - 1 >= 0 and dp[mid - 1] <= q:
                    #     temp = mid
                    # else:
                    #     temp = 0
                    # break
            result.append(temp)

        return result


        # 합을 내는 가장 긴 수열의 길이..
        # nums.sort() # 1 2 4 5
        # result = []
        # n = len(nums)
        # dp = [0 for _ in range(n)]
        # dp[0] = nums[0]
        # for i in range(1, n):
        #     dp[i] = dp[i - 1] + nums[i]
        # print(dp)
        # for q in queries:

        #     dp_ = [0 for _ in range(n)]
        #     for i in range(n):
        #         dp_[i] = abs(q - dp[i])
        #     print(dp_,'#')
        #     result.append(dp_.index(min(dp_)) + 1)
            # temp = 0
            # start = 0
            # end = n - 1
            # visited = [0 for _ in range(n)]
            # while(start <= end):
            #     mid = (start + end) // 2



            #     if mid >= n:
            #         break
            #     if dp[mid] == q and visited[mid] == 0:
            #         visited[mid] == 1
            #         temp = mid + 1
            #         break
            #     elif dp[mid] < q and visited[mid] == 0:
            #         visited[mid] == 1
            #         start += 1
            #     elif dp[mid] > q and visited[mid] == 0:
            #         visited[mid] == 1
            #         end -= 1
            # result.append(temp)


        # numLen = len(nums)
        # for q in queries:
        #     start = 0
        #     end = 1
        #     tempResult = []
        #     temp = nums[start] + nums[end]
        #     while(start < numLen and end < numLen):
        #         if temp == q:
        #             tempResult.append(end - start + 1)
        #             temp -= nums[start]
        #             start += 1
        #         elif temp < q:
        #             end += 1
        #             if end < numLen:
        #                 temp += nums[end]
        #         else:
        #             temp -= nums[start]
        #             start += 1
        #     if len(tempResult) != 0:
        #         result.append(max(tempResult))
        #     else:
        #         result.append(0)
        return result

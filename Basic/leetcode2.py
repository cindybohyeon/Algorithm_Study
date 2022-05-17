class Solution:
    
    
#     def IsCommon(self, strs, common, index):
        
#     for i in range(len(strs)):
#         if strs[i][index] == common:
#             continue
#         else:
#             return False
#     return True

    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        cursor = 0
        
        
#         check all of min str
#         check index element of all array element
            
#           check is there element in the same index

#           else second element of all array element 
#                 if there has no common return answer


        if not strs: #빈 배열이면
        	return ''
        minStr = min(strs, key = len)
        for i, x in enumerate(minStr):
        	for other in strs:
            	if other[i] != x:
                	return minStr[:i]
        return minStr
            
            


# def solution(citations):
#     answer = 0
#     citations.sort()
#     cLen = len(citations)
    
#     # 논문 n편 중 h번 이상 인용된 논문
#     hCase = []
#     # 3333
#     for i in range(cLen-1, 0, -1):
#         tempH = citations[i]
#         # (1) tempH 그리고 그 이상 값 체크
#         countH = cLen - i # 현재 개수
        
#         if countH >= tempH: # 6
#             # print(countH, tempH, "F")
#             hCase.append(countH)
            
    
# #         # (2) 현재 값과 같은 것 체크해야한다.
# #         for j in range(i - 1, 0, -1):
# #             if citations[j] == tempH:
# #                 countH += 1
                
# #         #countH = tempH 값 이상의 개수.        
        
# #         # 논문 개수가 tempH 이상있어야한다. 그리고 나머지
# #         # print(tempH, countH)
# #         if countH >= tempH:
# #             answer = tempH
# #             break
#     if hCase != []:
#         return max(hCase)
#     return answer


# # def solution(citations):
# #     citations = sorted(citations)
# #     l = len(citations)
# #     for i in range(l):
# #         if citations[i] >= l-i: # citations[i] 값보다 큰 것들이 
# #             print(citations[i] , l-i, "d")
# #             return l-i
# #     return 0




def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
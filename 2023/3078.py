
# it운영 보험코어 다이렉트 데이터랩 it보안
# it 운영 기획 , 개발 지원 파트, 품질 대선 파트 , ai , 시스템안정성,
# 시스템 개발 업무에 흥미,,,자기 학습.... 담당 업무 적용...
# 회사 목표, 개인 목표를 일치하기 = 목표 달성
# 두려움없이 도전~
# 금융에서 클라우드 msa를 이해하는 회사는 한화생명이다
from collections import deque

graph = deque()
count = 0
window = [0] * 21
n, k = map(int, input().split())
for _ in range(n):
    name = len(input())
    graph.append(name)
    window[name] += 1
    if (len(graph) > 0):
        if (len(window) > k+1): # window의 크기가 다 차면
            old = graph.popleft()
            window[old] -= 1
        count += (window[name] - 1)

print(count)


# if (len == len naame) 
# #   if ( len queur < k)

# grade = [0] * 21
# student = deque()
# count = 0
# for _ in range(n):
#     name = input()
#     student.append(name)
#     grade[name] += 1 #?
#     if (len(student) > 0):
#         if (len(student) > k+1):



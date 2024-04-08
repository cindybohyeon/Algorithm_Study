def solution(phone_book):
    answer = True
    
    hashMap = {}
    for p in phone_book:
        hashMap[p] = 1
    
    # 하나씩 증가시키면서 
    for p in phone_book: # 1000000
        temp = ""
        for num in p: # 20
            temp += num
            if temp in hashMap and temp != p:
                answer = False
            
    
    # phone_book.sort()   
    # sorted(phone_book)
    
    # lenPhone = len(phone_book)
    # print(phone_book)
    # 어떤 번호가 다른 번호의 접두어인 경우가 있으면?
    # 각 끝자리와 앞자리를 비교해야한다.
    # for i in range(lenPhone):
    #     for j in range(0, i): # 앞의 것만 보도록
    #         if phone_book[j] in phone_book[i]:
    #             p = phone_book[i]
    #             p2 = phone_book[j]
    #             # if p[0] == p2[0] and p[len(p2) -1] == p2[-1] and p != p2:
    #             if p.startswitch(p2):
    #                 # print(p, p2, "#")
    #                 answer = False
    #                 break
    
    
    # 배열의 위치, 존재 유무
        
    
    # endNumber = []
    # firstNumber = []
    # for number in phone_book:
    #     temp = number[-1]
    #     endNumber.append(temp)
    #     firstNumber.append(number[0])
    # lenPhone = len(phone_book)
    # for e in endNumber:
    #     for f in firstNumber:
    #         if e == f:
    #             answer = False
    #             break

    return answer
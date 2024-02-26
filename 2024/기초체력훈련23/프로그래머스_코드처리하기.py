def solution(code):
    answer = ''
    codeLen = len(code)
    mode = 0
    for i in range(codeLen):
        # print(mode,"mode", code[i])
        if mode == 0:
            if code[i] != '1':
                if i % 2 == 0:
                    # print("짝수", code[i])
                    answer += code[i]
            else:
                mode = 1
        else:
            if code[i] != '1':
                if i % 2 == 1:
                    answer += code[i]
            else:
                mode = 0
    if answer == '':
        return "EMPTY"
                
            
    return answer
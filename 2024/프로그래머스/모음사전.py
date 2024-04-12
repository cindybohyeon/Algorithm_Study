def solution(word):
    answer = 0
    allWords = []
    words = [ 'A', 'E', 'I', 'O', 'U', '']
    for a in words:
        for b in words:
            for c in words:
                for d in words:
                    for e in words:
                        temp = a+b+c+d+e
                        if temp not in allWords:
                            allWords.append(temp)
    allWords.sort()
    indexV = allWords.index(word)         
    
    # print(indexV)
    return indexV
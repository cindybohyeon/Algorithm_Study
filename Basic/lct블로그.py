# 중복제거하면서 insert , remove


from unittest import result


def insert(value, list):
    list.append(value)

    new_list = set(list)
    
    list = list(new_list)

    # return list

# def remove(value, list):

# list.remove(value)
# list.pop(index)




my_list = ['A', 'B','C']

# print(my_list)
# my_list = ['A', 'B', 'C', 'D', 'B', 'D', 'E']
# my_set = set(my_list) #집합set으로 변환
# my_list = list(my_set) #list로 변환
# print(new_list)
# insert("A", my_list)

# print(my_list)

arr = [1,2,3,4,4]
# dictionary 
def removeoverlap(arr):
    # using dictionary
    result = dict.fromkeys(arr)
    print(result)
    result2 = list(result)
    print(result2)

removeoverlap(arr)

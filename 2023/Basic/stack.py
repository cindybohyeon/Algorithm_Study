from cmath import exp
from ctypes import sizeof
from logging import exception
from sys import maxsize
from urllib.parse import MAX_CACHE_SIZE


def stack(str):
    s = empty stack
    for i = 0 ... i < str.size
        if str[i] == '('
            s.push()
        else
            if s.empty():
                return False
            s.pop()
        if s.empty():
            return True
        else:
            return False

#  배열은 stack

def push(arr,E):
    if arr.size == maxsize:
        throw exception()

    arr.append(E)

def pop(arr, E):
    if arr.size == 0:
        throw exception()
    last = arr[arr.size()-1]
    delete = arr[arr.size()-1]
    return last

    # 
    class Stack:
    def __init__(self):          # 빈 스택 하나를 생성합니다.
        self.items = []
                
    def push(self, item):        # 스택에 데이터를 추가합니다.
        self.items.append(item)
                
    def empty(self):             # 스택이 비어있으면 True를 반환합니다.
        return not self.items
                
    def size(self):              # 스택에 있는 데이터 수를 반환합니다.
        return len(self.items)
        
    def pop(self):               # 스택의 가장 위에 있는 데이터를 반환하고 제거합니다.
        if self.empty():
            raise Exception("Stack is empty")
            
        return self.items.pop()
                
    def top(self):               # 스택의 가장 위에 있는 데이터를 제거하지 않고 반환합니다.
        if self.empty():
            raise Exception("Stack is empty")
                        
        return self.items[-1]


# 변수 선언 및 입력:
n = int(input())
s = Stack()

for _ in range(n):
    command = input()
    
    if command.startswith("push"):
        x = int(command.split()[1])
        s.push(x)
    elif command.startswith("pop"):
        print(s.pop())
    elif command == "size":
        print(s.size())
    elif command == "empty":
        print(1 if s.empty() else 0)
    else:
        print(s.top())


        # 증가하는 수열 만들기 
function solution(arr)
  set s = empty stack
  for i = 0 ... i < arr.size
    set val = arr[i]
    if s.empty() == true or val > s.top():
      s.push(val)
      print(val)


# 시간복잡도
# 배열은 n
# 스택은 1, 큐도 1
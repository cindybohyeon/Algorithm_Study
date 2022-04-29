# arr = []
# while(1):
#     a = input()
#     if(a == "EOL"):
#         break
#     s2 = sorted(a)
#     s3 = ''.join(sorted(a))

#     arr.append(a)

# # 단어 w가 단어 v의 애너그램이 되려면 단어 w의 알파벳순서를 바꿔서 v를 만들 수 있어야 한다. 
# # 입력받은 string을 sort해서 만들어진 그룹 중 같으면 넣기. 


# # print(arr)

from unittest import result

class Solution:
   def groupAnagrams(self, strs):
      result = {}
      for i in strs:
         x = "".join(sorted(i))
         if x in result:
            result[x].append(i)
         else:
            result[x] = [i]
      return list(result.values())
      

      
ob1 = Solution()
print(ob1.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
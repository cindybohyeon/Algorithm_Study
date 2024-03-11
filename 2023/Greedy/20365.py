from pickletools import read_int4
import re


n = int(input())
color_list = list(input())
red, blue =0, 0
if color_list[0] == "B":
    blue += 1
else:
    red += 1
for i in range(1,n):
    if color_list[i] == "B" and color_list[i-1] == "R":
        blue += 1
        
    if color_list[i] == "R" and color_list[i-1] == "B":
        red += 1

# print(blue)
# print(red)

print(min(blue,red)+1)
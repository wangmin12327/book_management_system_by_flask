# str1 = input('')
# num1 = len(str1) % 8
# str2 = '0'
#
# if num1 != 0:
#     str1 = str1 + str2 * (8 - num1)
#
# i = 0
# while i <= len(str1):
#     print(str1[i:i+8])
#     i += 8



# import math
# n = int(input())
# for i in range(2, int(math.sqrt(n))+1):  #math.sqrt(n) ,返回n的平方根
#         print(i, end=' ')
#         n = n // i
# if n > 2:
#     print(n)

# n = int(input())
# Dict = {}
# while n > 0:
#     key = input()
#     value = input()
#     Dict.update({key, value})
#     n = n - 1
#     print(Dict)
#
# for key,value in Dict.items():
#     print(key,value)


# str1 = str(input())
# str2 = ''
# for i in range(len(str1)):
#     if str1[i].isalpha():
#         str2 += str1[i]
#     else:
#         str2 += ' '
# print(" ".join(str2.split()[::-1]))



# str1 = list(input())
# i = len(str1)-1
# class F:
#     index = ''
#     def __init__(self, index):
#         self.index = index
#     def f(self,index):
#         return ord(str1[index])
# Index = F(i)
# Result = Index.f(i)
# print(Result)









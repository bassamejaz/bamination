# runningCommand = ""
# while True:
#     userCommand = input().lower()
#     if userCommand == "help":
#         print('''
# Start - To start the car
# Stop - To stop the car
# Quit - To quit the game
#         ''')
#     elif userCommand == "start" and runningCommand != userCommand:
#         print("Car Started.. Ready to go")
#         runningCommand = userCommand
#     elif userCommand == "stop" and runningCommand != userCommand:
#         print("Car Stopped.")
#         runningCommand = userCommand
#     elif userCommand == "quit":
#         break
#     elif runningCommand == userCommand:
#         print("What are you doing")
#     else:
#         print("I dont understand that")
#
# # a,b = 0,1
# # while b<1000:
# #     print(b)
# #     a,b = b,a+b

# for x in range(0,11):
#     for y in range(x):
#         print("*",end="")
#     print("")
# for i in range(9,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print("")


# usercommand = int(input())
# for i in range(1,11):
#     ans = usercommand*i
#     print(usercommand,"x",i,"=",ans)

# for i in range(11):
#     ans  = "*"*i
#     print(ans)
# for y in range(9,0,-1):
#     ans2 = "*"*y
#     print(ans2)

# userinput = float(input())
# ans = ""
#
# def grade(userinput):
#     if userinput < 1 and userinput>0:
#         if userinput >= 0.9:
#             ans = "A"
#         elif userinput >= 0.8 and userinput < 0.9:
#             ans = "B"
#         elif userinput >= 0.7 and userinput < 0.8:
#             ans = "C"
#         elif userinput >= 0.6 and userinput < 0.7:
#             ans = "D"
#         elif userinput < 0.6:
#             ans = "F"
#     else:
#         ans = "Bad Score"
#     return ans
# print(grade(userinput))

# userinput = int(input())
# def facorial(userinput):
#     if userinput == 1:
#         return 1
#     else:
#         ans =  userinput*facorial(userinput-1)
#         return ans
# print(facorial(userinput))

# arr = [0,4,5,0,1,4,4]
# key = int(input())
# def find(arr,key):
#     count = 0
#     for i in range(len(arr)):
#         if arr[i] == key:
#             count += 1
#             index = i
#     print(count)
#     print(index)
#
# find(arr,key)
# import time
# def sel_sort(list):
#     size = len(list)
#     for i in range(size):
#         min = i
#         for j in range(i+1,size):
#           if list[j]<list[min]:
#               min = j
#         list[i],list[min] =list[min],list[i]
#     return list
#
# # list=[5,4,3,2,7,1,6]
# list1 = list(range(30000,0,-3))
# a  =time.time()
# sel_sort(list1)
# b = time.time()
# print(b-a)

# Python program for implementation of MergeSort




def bsearch(A,key):
    f_index = 0
    l_index = len(A)-1
    flag = 0
    while f_index <=l_index and flag == 0:
        mid =(f_index+l_index)//2
        if A[mid] == key:
            flag = mid
        elif key<A[mid]:
            l_index = mid-1
        else:
            f_index = mid+1
    return flag

list = [1,2,3,4,5,6,7,10]
bsearch(list,10)

import math
print(math.log2(20))










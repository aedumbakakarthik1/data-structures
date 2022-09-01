"""
recursion = a way od solving a promble by having a fuction calling itself

->performing the same operation multiple times with different input parameters
->in every step we try smaller input to mak the promblem samller
->based on conditions in neeeded to stop the recursive otherwise infinite loop will occour

code
def openRecssianDoll(doll) :
    if doll ==1:
        print("all doll are opened")
    else:
        openRecssianDoll(doll-1)

recursive thinking is really important in programming and it helps you break done big problems into smaller ones easier to use 


when to choose the recursive function ?
1)->if you can divide the problems into similar problems 
->design an algorithm to compute the nth
->implement a method to compute all
->practice


2)the prominent range of recursion in data structures like tree and graph
3)interview
4)it is used in many algorithm(divide and conquer,greedy and dynamic programming)

how recursion work ?
1)a method calls itself to
2)exit from infinite loop

code 

def recursionMethod():
    if exit from condition satisfies:
        return some value
    else:
        recursionMethod(modified parameter)




"""

def firstMethod():
    secondMethod()
    print("i am the first method")
def secondMethod():
    thirdMethod()
    print("i am the second method")
def thirdMethod():
    fourthMethod()
    print("i am the third method")
def fourthMethod():
    print("i am the fourth method")
print(firstMethod())

#best example
def recursionMethod(n):
    if n<1:
        print("n is less than 1")
    else:
        recursionMethod(n-1)
        print(n)
recursionMethod(4)

### here the  recursionMethod was always us the stack memory(first in last out)

"""when to use / avoid recursion ?
when to use ?
-> when we can easily breakdown a promblem into similar subproblem
->when we can fine with extha overhaed (both time and space ) that comes with it
-> when we need a quick working solution instead of efficiencyone
-> when we use tree to
-> when we use memoization in recursion

when we need to avoid ?
->if time and space complexity matters more
->recursion users more memory . if we use embbeded memory .For example an application that takes more memory in the phone in not efficient
->recurion ca be slow

"""



"""fibanacci number  - recursion
fibanacci squence is a squence of numbers in which each number the sum of two preceding ones and the squence atart froms 0 and 1 and

0,1,1,2,3,5,8,13,21,34,55,89....

"""
print("================================================")

def fibanacci(n):
    if n in [0,1]:
        return n
    else: 
        return fibanacci(n-1)+fibanacci(n-2)
print(fibanacci(6))
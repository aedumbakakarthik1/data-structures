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

"""when to use / avoid recursion ?"""
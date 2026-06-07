'''Q1. Practice Problem: Write a Python function that accepts two integer numbers.
 If the product of the two numbers is less than or equal to 1000,
 return their product; otherwise, return their sum.

Given Input:

Case 1: number1 = 20, number2 = 30
Case 2: number1 = 40, number2 = 30
Expected Output:

The result is 600
The result is 70
'''

def func(x,y):
    if(x*y<=1000):
        return x*y
    return x+y

# a=int(input("enter first num : "))
# b=int(input("enter second num : "))
# j=func(a,b)
# print("output : ",j)

'''Q2. Practice Problem: Iterate through the first 10 numbers (0–9). 
In each iteration, print the current number, the previous number, and their sum.'''

def loop():
    sum=0
    for i in range(10):
        if(i==0):
            print(f"current {i}, previous 0 : sum = 0")
            continue
        print(f"current {i}, previous{i-1} : sum = {i+(i-1)}")

loop()

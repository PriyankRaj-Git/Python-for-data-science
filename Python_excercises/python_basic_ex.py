'''Q1. Write a Python function that accepts two integer numbers.
 If the product of the two numbers is less than or equal to 1000,
 return their product; otherwise, return their sum.

Given Input:

Case 1: number1 = 20, number2 = 30
Case 2: number1 = 40, number2 = 30
Expected Output:

The result is 600
The result is 70
'''

def func1(x,y):
    if(x*y<=1000):
        return x*y
    return x+y

# a=int(input("enter first num : "))
# b=int(input("enter second num : "))
# j=func1(a,b)
# print("output : ",j)

'''Q2. Iterate through the first 10 numbers (0–9). 
In each iteration, print the current number, the previous number, and their sum.'''

def func2():
    sum=0
    for i in range(10):
        if(i==0):
            print(f"current {i}, previous 0 : sum = 0")
            continue
        print(f"current {i}, previous{i-1} : sum = {i+(i-1)}")

# func2()


'''Q3. Display only those characters which are 
present at an even index number in given string.'''

def func3(x):
    print(x[::2])

# func3("pineapple")


'''Q4. Write a function to remove characters from a string starting from
 index 0 up to n and return a new string.
 
 Given Input:

remove_chars("pynative", 4)
remove_chars("pynative", 2)
Expected Output:

tive
native
'''

def func4(x,n):
    s=""
    s=s+x[n:]
    return s

# j=func4("pynative",4)
# print(j)


'''Q5. Write a program to swap the values of two variables,
 a and b, without using a third temporary variable.
 Given Input: a = 5, b = 10

Expected Output:

Before Swap: a = 5, b = 10
After Swap: a = 10, b = 5
'''

def func5(x,y):
    return y,x

a,b=func5(10,20)
# print(a)
# print(b)


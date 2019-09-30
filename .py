def factorial(n):
    num=1
    while n>=1:
      num=num*n
      n=n-1
    return num
num1=int(input("Enter a number"))
print("factorial=",factorial(num1))
print("facotrial=")

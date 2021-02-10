print("CALCULATOR")
print('''1.SUM
2.SUB
3.MULTI
4.DIV
5.REM
7.ABS
6.EXPO (first number is the number and second number is the exponent to raised)''')

operation = input("Enter the operation: ").lower()
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

SUM = lambda a,b : a+b
SUB = lambda a,b : a-b
MULTI = lambda a,b : a*b
DIV = lambda a,b : a/b
REM = lambda a,b : a%b
ABS = lambda a : abs(a)
EXPO = lambda a,b : a**b

if operation == "sum":
    print("Result = ",SUM(first,second))
elif operation == "sub":
     print("Result = ",SUB(first,second))
elif operation == "multi":
    print("Result = ",MULTI(first,second))
elif operation == "div":
    print("Result = ",DIV(first,second))
elif operation == "rem":
    print("Result = ",REM(first,second))
elif operation == "abs":
    print("Result = ",ABS(first),",",abs(second))
elif operation == "expo":
    print("Result = ",EXPO(first,second))   
else:
    print("Inout not valid")



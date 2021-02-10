print('''ORDERING
1.MAX
2.MIN
3.ASCENDING
4.DESCENDING''')

type = input("Enter operation: ").lower()
numbers = input("Enter numbers: ")
number = numbers.split(",")

if type == "max":
    print("Result: ", max(number))
elif type == "min":
    print("Result: ", min(number))
elif type == "ascending":
    number.sort()
    print("Result: ", ", ".join(number))
elif type == "descending":
    number.sort()
    number.reverse()
    print("Result: ", ", ".join(number))
else:
    print("Invalid option.")

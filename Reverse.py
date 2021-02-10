name = input("Enter your name: ")
list = list(name)
list.reverse()
output = ""
for i in list:
    output += i
print(output)
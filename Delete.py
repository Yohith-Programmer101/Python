import os
target = "C:\\Users\\User\\Desktop\\PROGRAMS\\python\\Pycharm Project Files\\demo\\"
print()
for i in os.listdir(target):
    if i.endswith(".txt"):
        print("Files to be deleted:")
        print(target + i)
        print()
        inp = input("Do you want to delete it, this process can't be undone (yes or no): ")
        if inp == "yes":
            os.unlink(target + i)
        elif inp == "no":
            print("These files are not deleted.")
        else:
            print("I can't understand that.")
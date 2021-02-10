import os
response = os.popen("ipconfig")
file = open("text files\os.txt","w")
for i in response:
    file.write(i)
file.close()
# redirects cmd operations to text files\os.txt
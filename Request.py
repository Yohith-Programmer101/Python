import requests
res = requests.get("http://automatetheboringstuff.com/files/rj.txt")
res.raise_for_status() # it will return nothing if there the location is correct
file = open("c:\\Users\\User\\Desktop\\PROGRAMS\\python\\Pycharm Project Files\\text files\\request.txt", "wb") # we should write in the form of binary data
for chumk in res.iter_content(10000):
    file.write(chumk)
file.close()
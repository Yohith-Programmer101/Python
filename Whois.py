import whois, os
host = "google.com"
os.chdir("text files")
res = whois.whois(host)
file = open("whois.txt", "w")
print(res)
file.write(str(res))
print("=" * 100)
file.write("=" * 100)
for x in res:
    print(x)
    file.write(x + "\n")
print("=" * 100)
file.write("=" * 100 +"\n" )
for i in res.expiration_date:
    print(i)
    file.write(str(i) + "\n")
print("=" * 100 + "\n")
file.write("=" * 100 + "\n")
file.close()
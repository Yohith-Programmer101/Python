import whois
import sys

inp = input("Enter Domain to check: ")

try:
    domain = whois.whois(inp)
    if domain.domain_name == None:
        sys.exit(1)
except:
    print("Domain available")
else:
    print("Domain taken")
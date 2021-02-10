import requests
from bs4 import BeautifulSoup

print("=" * 100)
search_query = input("Enter keyword to search in google.com: ")
result = requests.get(f"https://google.com/search?q={search_query}")
soup = BeautifulSoup(result.text, "html.parser")
print(soup)
print("=" * 100)
print("\n")
print("=" * 100)
search_query = input("Enter keyword to search in youtube.com: ")
result = requests.get(f"https://www.youtube.com/results?search_query={search_query}")
soup = BeautifulSoup(result.text, "html.parser")
print(soup)
print("=" * 100)
print("\n")
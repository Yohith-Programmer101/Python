import os
import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=34.09969000000007&lon=-118.33512999999999#.X3csgGgzbIU")
soup = BeautifulSoup(page.content, "html.parser")

# print(soup) # returns the full html code of the page
# print(soup.find_all("a")) # returns all the a tags in the html code

week = soup.find(id = "seven-day-forecast-body")
# print(week)

items = week.find_all(class_= "tombstone-container")
# print(items[0])

# print(items[0].find(class_="period-name").get_text())
# print(items[0].find(class_="short-desc").get_text())
# print(items[0].find(class_="temp").get_text())

period_names = [item.find(class_="period-name").get_text() for item in items]
short_desc = [item.find(class_="short-desc").get_text() for item in items]
temperatures = [item.find(class_="temp").get_text() for item in items]

# print(period_names)
# print(short_desc)
# print(temperatures)

weather_stuff = pd.DataFrame(
    {
       "period":period_names,
        " short_descriptions":short_desc,
        "temperatures":temperatures
    })

print(weather_stuff)

os.chdir("documents")
weather_stuff.to_csv("beatifulsoup.csv")
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
os.chdir("webdrivers")
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("http://communication-bot.rf.gd")
browser.find_element_by_link_text("Invite").click()
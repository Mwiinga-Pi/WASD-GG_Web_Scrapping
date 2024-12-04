import selenium
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.edge.service import Service
from msedge.selenium_tools import Edge, EdgeOptions
import time

# options = webdriver.EdgeOptions
#options.use_chromium = True
# options.add_argument(r"--user-data-dir =C:\Users\Mwiinga.Nathan\AppData\Local\Microsoft\Edge\User Data")
# options.add_argument(r"profile-directory=Default")
# driverpath = "msedgedriver.exe"

#srv = "C:\Users\Mwiinga.Nathan\OneDrive - West Ada School District\Desktop\Code\msEdgeDriver\msedgedriver.exe"

driver = webdriver.Edge(options=webdriver.edgeoptions)


targetSite = 'https://www.westada.org'
driver.get(targetSite)

time.sleep(30)
driver.quit()
##  Using https://learn.microsoft.com/en-us/microsoft-edge/webdriver-chromium/?tabs=python

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

desiredSleepTime = 1

options = webdriver.EdgeOptions()
options.add_argument(r"--ser-data-dir=C:\Users\Mwiinga.Nathan\AppData\Local\Microsoft\Edge\User Data")
options.add_argument("--profile-directory=Default")
options.add_argument("--start-maximized")

driver = webdriver.Edge(options=options)

# driver = Edge(executable_path=r"C:\Users\Mwiinga.Nathan\OneDrive - West Ada School District\Desktop\Code\msEdgeDriver\msedgedriver.exe",options=opt)
targetSite = r"https://account.goguardian.com/#/?referral=https%3A%2F%2Fadmin.goguardian.com%3Fauth_redirect%3Dtrue"
targetGroupSite = r"https://admin.goguardian.com/groups/17014"
driver.get(targetSite)

# Select Google login option
time.sleep(desiredSleepTime)
element = driver.find_element(By.CLASS_NAME, "google-signin-button")
# element = driver.find_element(By.XPATH, "//a[@class='google-signin-button']")
element.click()

#enter User Email Address
time.sleep(desiredSleepTime)
userEmailSelection = driver.find_element(By.CLASS_NAME,"whsOnd")
userEmailSelection.send_keys("mwiinga.nathan@westada.org", Keys.ENTER)

#enter User Email Password
time.sleep(desiredSleepTime*3)
userEmailSelection = driver.find_element(By.CLASS_NAME,"whsOnd")
time.sleep(desiredSleepTime*30)
# userEmailSelection.send_keys(Keys.ENTER)
# advancePage = driver.find_element(By.CLASS_NAME,"VfPpkd-vQzf8d")
# advancePage.click()


# Next Steps
# go to the groups page in GG, or direct open the specific group.
# EDIT: No do while loop in python, explore this --> https://www.geeksforgeeks.org/python-do-while/
#       ... and this: https://www.selenium.dev/documentation/webdriver/elements/finders/
# DO {
#   Grab items from <ul> block
#   Grabed items: User, Org Unit, Added On, Added By
# } WHILE (<li tile="Next Page" !contain 'ant-pagination-disabled')
# driver.get(targetGroupSite)

time.sleep(desiredSleepTime*3)
custonGroupSelection = driver.find_element(By.LINK_TEXT,"Custom Groups" )
custonGroupSelection.send_keys(Keys.ENTER)

time.sleep(desiredSleepTime*3)
specifiedGroupSelection = driver.find_element(By.LINK_TEXT,"Internet Limited")
specifiedGroupSelection.send_keys(Keys.ENTER)

time.sleep(desiredSleepTime*3)
tableData = driver.find_elements(By.CLASS_NAME, "v5-row-level-0")

userRowData = driver.find_element(By.CLASS_NAME, "v5-row-level-0")
userColData = userRowData.find_elements(By.CSS_SELECTOR, ".sc-gsnTZi.fqXKKX")

content =[]
content.append([rowData.text for rowData in userColData])
print(content)
# for d in tableData:
    # print(d.text)

time.sleep(desiredSleepTime*3)
while(True):
    print("Get User, Org Unit, Added On, Added By from Each <li>")
    # pageNext = driver.find_elements(By.CSS_SELECTOR, "ant-pagination-next")
    targetElement = driver.find_elements(By.CSS_SELECTOR, ".ant-pagination-next.ant-pagination-disabled")
    if len(targetElement) == 0: # if that element is empty, means that there is more pages
        print("there is more paginations to look at. Stand by...")
        nextPagination = driver.find_element(By.CLASS_NAME, "ant-pagination-next")
        nextPagination.send_keys(Keys.ENTER)
        time.sleep(desiredSleepTime*3)
        
        tableData = driver.find_elements(By.CLASS_NAME, "v5-row-level-0")
        content.append(str([rowData.text for rowData in tableData]))

        continue
        
    else:
        print("there is NO MORE paginations to look at. GoodBye")
        
        # <li tile="Next Page" !contain 'ant-pagination-disabled'
        break

print(content)
time.sleep(60)
driver.quit()
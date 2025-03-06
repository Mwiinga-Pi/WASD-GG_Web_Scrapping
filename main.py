##  Using https://learn.microsoft.com/en-us/microsoft-edge/webdriver-chromium/?tabs=python

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

import csv

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
time.sleep(desiredSleepTime*20)
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
specifiedGroupSelection = driver.find_element(By.LINK_TEXT,"Internet Limited") #You can target a specific group by name here!
specifiedGroupSelection.send_keys(Keys.ENTER)

time.sleep(desiredSleepTime*3)
tableData = driver.find_elements(By.CLASS_NAME, "v5-row-level-0") # gets all the rows from the table

userRowData = driver.find_element(By.CLASS_NAME, "v5-row-level-0")
# userNameOrgUnitData = userRowData.find_elements(By.CSS_SELECTOR, ".sc-gsnTZi.fqXKKX") #student Name and Org unit
# userAddedInfo= userRowData.find_elements(By.CSS_SELECTOR, ".v5-cell.v5-column-sort") #added on column
# studentEmail= userRowData.find_elements(By.CSS_SELECTOR, ".sc-dSqHuY.dJebBY") #student email

# print(userNameOrgUnitData)
# print(studentEmail)
content =[]

studentNameCSS_Selector = ".sc-jqUVSM.gcZKBE"
addedOnCSS_Selector = ".v5-cell.v5-column-sort"
studentNameCSS_Selector = ".sc-keNpes.ltfIc"

for eachRow in tableData:
    tempList = []
    rowColumns = eachRow.find_elements(By.CLASS_NAME, "v5-cell") # creates a list 7 items long w/ all fields
                                                                #   Only need items 1, 2, 4, and 5 (ignore index 0, 6)
    tempList.append(rowColumns[1].text.split("\n")[0]) # name
    tempList.append(rowColumns[1].text.split("\n")[1]) # email
    tempList.append(rowColumns[2].text) # Org unit
    tempList.append(rowColumns[4].text) # Added on date
    tempList.append(rowColumns[5].text) # Added by
    print(tempList)
    content.append(tempList)

for rowData in tableData:
    tempList = []
    userNameOrgUnitData = rowData.find_elements(By.CSS_SELECTOR, studentNameCSS_Selector) #student Name and Org unit
    userAddedInfo= rowData.find_elements(By.CSS_SELECTOR, addedOnCSS_Selector) #added on column
    studentEmail= rowData.find_elements(By.CSS_SELECTOR, studentNameCSS_Selector) #student email

    for rowData in userNameOrgUnitData:
        tempList.append(rowData.text)
    for rowData in userAddedInfo:
        tempList.append(rowData.text)
    for rowData in studentEmail:
        tempList.append(rowData.text)
    print(tempList)
    content.append(tempList)



# content.append(str( [rowData.text for rowData in tableData]))

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
        for rowData in tableData:
            tempList = []
            userNameOrgUnitData = rowData.find_elements(By.CSS_SELECTOR, studentNameCSS_Selector) #student Name and Org unit
            userAddedInfo= rowData.find_elements(By.CSS_SELECTOR, addedOnCSS_Selector) #added on column
            studentEmail= rowData.find_elements(By.CSS_SELECTOR, studentNameCSS_Selector) #student email

            for rowData in userNameOrgUnitData:
                tempList.append(rowData.text)
            for rowData in userAddedInfo:
                tempList.append(rowData.text)
            for rowData in studentEmail:
                tempList.append(rowData.text)
            print(tempList)
            content.append(tempList)
        # print(content)
        # content.append(str([rowData.text for rowData in tableData]))

        continue
        
    else:
        print("there is NO MORE paginations to look at. GoodBye")
        
        # <li tile="Next Page" !contain 'ant-pagination-disabled'
        break

print(content)
outputCsvPath = r"C:\Users\Mwiinga.Nathan\OneDrive - West Ada School District\Desktop\Code\WebScraper\outputFile.csv"
with open(outputCsvPath, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(content)
print("CSV Created.")
time.sleep(6)

driver.quit()

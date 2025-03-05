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
driver.get(targetSite)

# Select Clever login option to utilize SSO
time.sleep(desiredSleepTime)
element = driver.find_element(By.CLASS_NAME, "clever-signin-button")
# element = driver.find_element(By.XPATH, "//a[@class='google-signin-button']")
element.click()

# logging into a WASD school
time.sleep(desiredSleepTime)
userEmailSelection = driver.find_element(By.CSS_SELECTOR,".Autosuggest--textInput.Autosuggest--textInput--focusable")
userEmailSelection.send_keys("West Ada School District")
time.sleep(desiredSleepTime*4)
userEmailSelection.send_keys(Keys.ENTER)

# logging in through entra via a district admin user
time.sleep(desiredSleepTime*3)
userEmailSelection = driver.find_element(By.CSS_SELECTOR,".flexbox.items--center.AuthMethod--container")
userEmailSelection.send_keys(Keys.ENTER)
time.sleep(desiredSleepTime*3)
# districtAdminLogin = driver.find_elements(By.PARTIAL_LINK_TEXT, "district admin")
districtAdminLogin = driver.find_element(By.XPATH, "//button[text()='Log in as a district admin']")
# districtAdminLogin = driver.find_elements(By.CLASS_NAME, "auth-method-button")
districtAdminLogin.send_keys(Keys.ENTER)
time.sleep(desiredSleepTime*30)
# userEmailSelection.send_keys(Keys.ENTER)
# advancePage = driver.find_element(By.CLASS_NAME,"VfPpkd-vQzf8d")
# advancePage.click()

def loopGGPullGroups(groupName):
    time.sleep(desiredSleepTime*3)
    specifiedGroupSelection = driver.find_element(By.LINK_TEXT, groupName)
    specifiedGroupSelection.send_keys(Keys.ENTER)

    time.sleep(desiredSleepTime*3)
    tableData = driver.find_elements(By.CLASS_NAME, "v5-row-level-0")

    userRowData = driver.find_element(By.CLASS_NAME, "v5-row-level-0")
    # userNameOrgUnitData = userRowData.find_elements(By.CSS_SELECTOR, ".sc-gsnTZi.fqXKKX") #student Name and Org unit
    # userAddedInfo= userRowData.find_elements(By.CSS_SELECTOR, ".v5-cell.v5-column-sort") #added on column
    # studentEmail= userRowData.find_elements(By.CSS_SELECTOR, ".sc-dSqHuY.dJebBY") #student email

    # print(userNameOrgUnitData)
    # print(studentEmail)
    content =[]


    for rowData in tableData:
        tempList = []
        userNameOrgUnitData = rowData.find_elements(By.CSS_SELECTOR, ".sc-gsnTZi.fqXKKX") #student Name and Org unit
        userAddedInfo= rowData.find_elements(By.CSS_SELECTOR, ".v5-cell.v5-column-sort") #added on column
        studentEmail= rowData.find_elements(By.CSS_SELECTOR, ".sc-dSqHuY.dJebBY") #student email

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
                userNameOrgUnitData = rowData.find_elements(By.CSS_SELECTOR, ".sc-gsnTZi.fqXKKX") #student Name and Org unit
                userAddedInfo= rowData.find_elements(By.CSS_SELECTOR, ".v5-cell.v5-column-sort") #added on column
                studentEmail= rowData.find_elements(By.CSS_SELECTOR, ".sc-dSqHuY.dJebBY") #student email

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

# Next Steps
# go to the groups page in GG, or direct open the specific group.
# EDIT: No do while loop in python, explore this --> https://www.geeksforgeeks.org/python-do-while/
#       ... and this: https://www.selenium.dev/documentation/webdriver/elements/finders/
# DO {
#   Grab items from <ul> block
#   Grabed items: User, Org Unit, Added On, Added By
# } WHILE (<li tile="Next Page" !contain 'ant-pagination-disabled')
# driver.get(targetGroupSite)

time.sleep(desiredSleepTime*15)
custonGroupSelection = driver.find_element(By.LINK_TEXT,"Custom Groups" )
custonGroupSelection.send_keys(Keys.ENTER)

time.sleep(desiredSleepTime*3)
specifiedGroupSelection = driver.find_element(By.LINK_TEXT,"Internet Limited")
specifiedGroupSelection.send_keys(Keys.ENTER)

time.sleep(desiredSleepTime*3)
tableData = driver.find_elements(By.CLASS_NAME, "v5-row-level-0")

userRowData = driver.find_element(By.CLASS_NAME, "v5-row-level-0")
# userNameOrgUnitData = userRowData.find_elements(By.CSS_SELECTOR, ".sc-gsnTZi.fqXKKX") #student Name and Org unit
# userAddedInfo= userRowData.find_elements(By.CSS_SELECTOR, ".v5-cell.v5-column-sort") #added on column
# studentEmail= userRowData.find_elements(By.CSS_SELECTOR, ".sc-dSqHuY.dJebBY") #student email

# print(userNameOrgUnitData)
# print(studentEmail)
content =[]


for rowData in tableData:
    tempList = []
    userNameOrgUnitData = rowData.find_elements(By.CSS_SELECTOR, ".sc-gsnTZi.fqXKKX") #student Name and Org unit
    userAddedInfo= rowData.find_elements(By.CSS_SELECTOR, ".v5-cell.v5-column-sort") #added on column
    studentEmail= rowData.find_elements(By.CSS_SELECTOR, ".sc-dSqHuY.dJebBY") #student email

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
            userNameOrgUnitData = rowData.find_elements(By.CSS_SELECTOR, ".sc-gsnTZi.fqXKKX") #student Name and Org unit
            userAddedInfo= rowData.find_elements(By.CSS_SELECTOR, ".v5-cell.v5-column-sort") #added on column
            studentEmail= rowData.find_elements(By.CSS_SELECTOR, ".sc-dSqHuY.dJebBY") #student email

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
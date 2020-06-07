from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
# defining object
browser = webdriver.Chrome('/home/nomercy990/PycharmProjects/applyingthejobs/driver/chromedriver')
browser.get('https://www.randstadusa.com/')
browser.maximize_window()
#######################
# login part
#######################
# clicking the login link
loginMain = browser.find_element_by_xpath('//*[@id="ctl09_ctl00_LinkLoginList"]/a')
browser.implicitly_wait(5)
loginMain.click()
browser.implicitly_wait(5)
# cookies accept
cookiesButton = browser.find_element_by_xpath('//*[@id="hs-eu-confirmation-button"]')
cookiesButton.click()
# login
loginField = browser.find_element_by_xpath('//*[@id="content"]/div/div[6]/div/div/div[2]/div/cicp-signin/div/div[4]/div/div/div[1]/div/div/input')
loginField.click()
loginField.send_keys('''youremail@mail.com''')
# password
passwordField = browser.find_element_by_xpath('//*[@id="content"]/div/div[6]/div/div/div[2]/div/cicp-signin/div/div[4]/div/div/div[2]/div/div/input')
passwordField.click()
passwordField.send_keys('''Any@typeofPassword123''')
# pressing the login button
button = browser.find_element_by_xpath('//*[@id="content"]/div/div[6]/div/div/div[2]/div/cicp-signin/div/div[4]/div/div/div[4]/div/div/div/button/div[2]')
button.click()
time.sleep(3)
#######################
# end of the login part
#######################
# switching to the search page
browser.implicitly_wait(5)
searchButton = browser.find_element_by_xpath('//*[@id="sbm_jobs"]/li[1]/a')
searchButton.click()
browser.implicitly_wait(5)
# clearing the zipcode/adding location if needed
jobLocation = browser.find_element_by_xpath('//*[@id="JobSearchLocationTextBox"]')
jobLocation.clear()
# uncomment this line if need the region --> jobLocation.sendkeys('yourZipCode')
# switching to the job title for the search
jobKeywords = browser.find_element_by_xpath('//*[@id="JobSearchKeywordsTextBox"]')
jobKeywords.send_keys('automation python')
# submitting the request
submitButton = browser.find_element_by_xpath('//*[@id="ctl07_ctl03_JobSearchSubmitLinkButton"]')
submitButton.click()
# changing the page job listing to 50
browser.implicitly_wait(5)
browser.find_element_by_xpath('//*[@id="ctl08_ctl03_JobsPerPageDropDownList"]').click()
browser.find_element_by_xpath('//*[@id="ctl08_ctl03_JobsPerPageDropDownList"]/option[3]').click()
browser.implicitly_wait(5)
for x in range(50):
    valueXpath = 0
    browser.implicitly_wait(5)
    currentJob = browser.find_element_by_xpath('//*[@id="ctl08_ctl03_JobsListView_ctrl'+str(valueXpath)+'_JobTitleHyperLink"]')
    currentJob.click()
    browser.implicitly_wait(5)
    easyApply = browser.find_element_by_xpath('//*[@id="ltrlApplyNowTop"]/a')
    easyApply.click()
    dropDown = browser.find_element_by_xpath('//*[@id="ctl07_ctl03_ApplyTopLinkButton"]')
    dropDown.click()
    browser.implicitly_wait(5)
    lastButton = browser.find_element_by_xpath('//*[@id="ctl07_ctl03_ApplyFormDiv"]/div[2]/application/div/div/div/div/div[8]/div/div/div/div/div[2]/button/div[2]')
    lastButton.click()
    time.sleep(3)
    valueXpath += 2
    time.sleep(3)
    print("Applied for the job!")

#importing the libraries


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# get the path of ChromeDriverServer

chrome_driver_path = r"C:\Users\user\Downloads\chromedriver.exe"

# create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(20)  #implicit wait for the driver incase the page/element load is slow
driver.maximize_window() #maximise the window

# Navigate to the application home page
driver.get(r"C:\Users\user\PycharmProject\interview\TASK1\index.html")
#Destination path
dest_element1 = driver.find_element_by_xpath('//*[@id="sortable"]/tr[8]/td[1]')
#different source xpaths for different elements to be dragged
source_element1 = driver.find_element_by_xpath('//*[@id="sortable"]/tr[2]/td[1]')
#Performing drag and drop
#for the next drop location the current source will be xpath
action = ActionChains(driver) # initialize action

action.drag_and_drop(source_element1,dest_element1).perform() #performing drag and drop from soruce to destination element

source_element2 = driver.find_element_by_xpath('//*[@id="sortable"]/tr[2]/td[1]')
action.drag_and_drop(source_element2,source_element1).perform()

source_element3 = driver.find_element_by_xpath('//*[@id="sortable"]/tr[1]/td[1]')
action.drag_and_drop(source_element3,source_element2).perform()

source_element4 = driver.find_element_by_xpath('//*[@id="sortable"]/tr[1]/td[1]')
action.drag_and_drop(source_element4,source_element3).perform()

source_element5 = driver.find_element_by_xpath('//*[@id="sortable"]/tr[3]/td[1]')
action.drag_and_drop(source_element5,source_element4).perform()

source_element6 = driver.find_element_by_xpath('//*[@id="sortable"]/tr[2]/td[1]')
action.drag_and_drop(source_element6,source_element5).perform()

source_element7 = driver.find_element_by_xpath('//*[@id="sortable"]/tr[1]/td[1]')
action.drag_and_drop(source_element7,source_element6).perform()

source_element8 = driver.find_element_by_xpath('//*[@id="sortable"]/tr[1]/td[1]')
action.drag_and_drop(source_element8,source_element7).perform()


source_element7 = driver.find_element_by_xpath('//*[@id="sortable"]/tr[1]/td[1]')
action.click_and_hold(source_element7)
action.move_to_element(source_element6).release().perform()

#final element to be sorted
source_element8 = driver.find_element_by_xpath('//*[@id="sortable"]/tr[1]/td[1]')
action.click_and_hold(source_element8)
action.move_to_element(source_element7).release().perform()

#sorting is done
print("Sorted")



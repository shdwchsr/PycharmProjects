from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# import openpyxl as excel

driver = webdriver.Chrome('C:/Users/User1/PycharmProjects/whatsapp_template/chromedriver.exe')

driver.get("https://web.whatsapp.com/")

wait = WebDriverWait(driver, 600)

#

target = '"+65 8145 2671"'
# Replace the below string with your own message
string = "Test"

## path to search by Contact
# x_arg = '//span[contains(@title,' + target + ')]'
x_arg = '//span[contains(@class="_1X4JR",' + target + ')]'
print(x_arg)
group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
print(group_title)
group_title.click()

# path to search by Name
inp_xpath = '//div[@class="_3FRCZ copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'

input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
for i in range(1):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)

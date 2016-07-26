#! python
from selenium import webdriver
import time ,re, sys
from selenium.webdriver.common.keys import Keys
if(len(sys.argv) >= 2):
    code = sys.argv[1]
else:
    print("Please enter a code")
    code = input()
pattern = re.compile(r'(\d{5})-(\d{5})-(\d{5})-(\d{5})-(\d{5})-(\d)')
while(not pattern.match(code)):
    print("code invalid! : Reenter")
    code = input()

print("Accepted!!")

driver = webdriver.Firefox()
driver.get('https://mcdvoice.com')
clickHere = driver.find_element_by_link_text("click here.")
print("clicking....")
clickHere.click()
time.sleep(2)

groups = pattern.search(code)
formFields = ['CN1', 'CN2', 'CN3', 'CN4','CN5','CN6']
for i in range(1, len(formFields)+1):
    field = driver.find_element_by_id(formFields[i-1])
    field.send_keys(groups.group(i))
    print('{0} : {1}'.format(i, groups.group(i)))
print("submiting for validation....")
while(True):
    try:
        start = driver.find_element_by_id("NextButton")
        start.click()
    except:
        validation = driver.find_element_by_class_name('ValCode')
        print(validation.text)
        break;
driver.close()

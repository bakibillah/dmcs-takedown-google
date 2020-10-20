from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from time import sleep


text1 = 'The photographs of the black widow spider with red spots and that of the black labrador retriever which can be viewed at the URL below” or “My published book, “Touch Not This Cat”, is infringed by the text excerpted on the site, beginning with the text ‘I came home to find my cat sitting on the kitchen counter'
my_url = 'udemy.com'
infringement_url = 'freecoursesite.com'


def define_options():
    options = Options()
    options.add_argument("--start-maxiized")
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--window-size=1850,1050")
    options.add_experimental_option('excludeSwitches', ['load-extension', 'enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"')
    options.add_argument("user-data-dir=C:\\Users\\samir\\AppData\\Local\\Google\\Chrome\\User Data")
    driver_ = webdriver.Chrome(options=options)
    # driver = webdriver.Firefox(options=options)
    return driver_


driver = define_options()
driver.get('https://support.google.com/legal/troubleshooter/1114905')
sleep(1)
radio = driver.find_element(By.XPATH, "//div[@class='main-content']/article/section/div/div[2]/div/label[1]/input")
driver.execute_script("arguments[0].click();", radio)
sleep(1)
select_search = driver.find_element(By.XPATH, "//div[@class='main-content']/article/section/div/div[2]/div[2]/div/label/input")
driver.execute_script("arguments[0].click();", select_search)
sleep(1)
Intellectual_property = driver.find_element(By.XPATH, "//div[@class='main-content']/article/section/div/div[2]/div[2]/div[3]/div[2]/label[4]/input")
driver.execute_script("arguments[0].click();", Intellectual_property)
sleep(1)

Copyright_infringement = driver.find_element(By.XPATH, "//div[@class='main-content']/article/section/div/div[2]/div[2]/div[2]/div[7]/div[2]/label/input")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", Copyright_infringement)

sleep(1)
driver.execute_script("arguments[0].click();", Copyright_infringement)
sleep(2)
authorized = driver.find_element(By.XPATH, "//div[@class='main-content']/article/section/div/div[2]/div[2]/div[2]/div[7]/div[3]/div/label[1]/input")
sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", authorized)
sleep(1)
driver.execute_script("arguments[0].click();", authorized)
sleep(2)
other = driver.find_element(By.XPATH, "//div[@class='main-content']/article/section/div/div[2]/div[2]/div[2]/div[7]/div[3]/div[2]/div/label[2]/input")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", other)
sleep(1)
driver.execute_script("arguments[0].click();", other)
sleep(2)
create_request = driver.find_element(By.XPATH, "//a[contains(text(),'Create request')]")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", create_request)
sleep(1)
driver.execute_script("arguments[0].click();", create_request)
sleep(2)
first_name = driver.find_element(By.NAME, "first-name")
first_name.send_keys('Baki')
last_name = driver.find_element(By.NAME, "last-name")
last_name.send_keys('Billah')
company_name = driver.find_element(By.NAME, "company-name")
sleep(1)
company_name.send_keys('Udemy Inc')
sleep(1)
select = Select(driver.find_element_by_name('cr-holder'))
select.select_by_value('self')
sleep(1)
confirm_self = driver.find_element(By.ID, "confirm-self-cr-holder").click()
sleep(1)
email = driver.find_element(By.NAME, "email")
email.send_keys('mdbakibillah@gmail.com')
sleep(1)
country_code = Select(driver.find_element_by_name('country-code'))
country_code.select_by_value('BD')
sleep(1)
isLivestream = Select(driver.find_element_by_name('isLivestream'))
isLivestream.select_by_value('false')
sleep(1)
textarea1 = driver.find_element(By.XPATH, "//div[@id='webform']/div/div/div/div/textarea[@name='cr-work-desc0']")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", textarea1)
sleep(1)
textarea1.send_keys(text1)
sleep(2)
textarea2 = driver.find_element(By.XPATH, "//div[@id='webform']/div/div/div/div/textarea[@name='cr-work-urls0']")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", textarea2)
sleep(1)
textarea2.send_keys(my_url)
sleep(2)

textarea3 = driver.find_element(By.XPATH, "//div[@id='webform']/div/div/div/div/textarea[@name='infringing-urls0']")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", textarea3)
sleep(1)
textarea3.send_keys(infringement_url)
sleep(2)

tick_1 = driver.find_element(By.NAME, "agree2").click()
sleep(1)
tick_2 = driver.find_element(By.NAME, "agree1").click()
sleep(1)
tick_3 = driver.find_element(By.NAME, "agree5").click()
sleep(1)

signature_date = driver.find_element(By.NAME, "signature-date").send_keys('20-10-2020')
sleep(1)
signature = driver.find_element(By.NAME, "signature").send_keys('baki billah')
sleep(10)

# WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
sleep(6)
driver.quit()

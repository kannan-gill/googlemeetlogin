import time

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from selenium.webdriver.chrome.options import Options

#this next section is very important to give camera and microphone permissions. Without this, the code will not work.

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")

opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
  })

driver = webdriver.Chrome(chrome_options=opt)

#open gmail login
driver.get("https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin")

#login to google
username=driver.find_element_by_name("identifier")
username.send_keys("<<--YOUR E-MAIL ID-->>")
nextbutton=driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]")
nextbutton.click()
time.sleep(4)
password=driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
password.send_keys("<<--YOUR PASSWORD-->>")
sub=driver.find_element_by_xpath("//*[@id='passwordNext']/div/button/div[2]")
sub.click()
time.sleep(4)

#redirect to google meet 
driver.get("<<--GOOGLE MEET ID-->>")
time.sleep(4)

#switch off mic and camera before turning on the meet
driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div").click()
time.sleep(5)
        
driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div").click()
time.sleep(5)
join=driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span")
join.click()
#change this time according to class length
time.sleep(10)
#log out of the class
driver.get("https://www.google.com/")
time.sleep(5)
driver.quit()



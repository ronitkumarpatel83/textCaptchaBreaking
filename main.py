import time
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytesseract


chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()

loginBtn = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[1]/app-header/div[2]/div[2]/div[1]/a[1]')
driver.execute_script("arguments[0].click();", loginBtn)
userName = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[1]/input')
passWord = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[2]/input')
userName.send_keys('ronitsdet07')
passWord.send_keys('Patel@12345')

time.sleep(2)
element = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[4]/div/app-captcha/div/div/div[2]/span[1]/img')
element.screenshot("captchaImage/captcha.png")

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Load CAPTCHA image
captcha_image = Image.open('captchaImage/captcha.png')
captcha_text = pytesseract.image_to_string(captcha_image)
print("Extracted CAPTCHA text:", captcha_text)

captchaInput = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[4]/div/app-captcha/div/div/input')
captchaInput.send_keys(captcha_text)
time.sleep(5)
time.sleep(2)

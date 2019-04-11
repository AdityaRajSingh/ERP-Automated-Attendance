from bs4 import BeautifulSoup
import requests
import urllib.request
from pytesseract import image_to_string 
from PIL import Image

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

br = webdriver.Firefox()
url = r"http://erp.bitmesra.ac.in/iitmsv4eGq0RuNHb0G5WbhLmTKLmTO7YBcJ4RHuXxCNPvuIw=?enc=EGbCGWnlHNJ/WdgJnKH8DA=="
br.get(url)
#br.set_window_size(1120, 550)



def get_captcha_text(location, size):
    #pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
    im = Image.open('screenshot.png') # uses PIL library to open image in memory

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']


    im = im.crop((left, top, right, bottom)) # defines crop points
    im.save('screenshot.png')
    captcha_text = image_to_string(Image.open('screenshot.png'))
    return captcha_text

element = br.find_element_by_xpath('//*[@id="frmDefault"]/div[3]/div/div[4]/div[1]/div[2]/img')
location = element.location    
size = element.size    
br.save_screenshot('screenshot.png')


search_form_password = None
search_form_username = None

while search_form_password == None or search_form_username == None:
    search_form_username = br.find_element_by_class_name('form-section').find_element_by_name('txt_username')
    search_form_password = br.find_element_by_class_name('form-section').find_element_by_name('txt_password')
    print (search_form_username)
    print (search_form_password)
    



search_form_username.send_keys(open(r"username.txt",'r').read())
search_form_password.send_keys(open(r"password.txt",'r').read())

captcha = br.find_element_by_xpath('//*[@id="txtcaptcha"]')
captcha.clear()
captcha_text = get_captcha_text(location, size)
captcha.send_keys(captcha_text)

search_form_submit = br.find_element_by_class_name('form-section').find_element_by_id('btnSubmit')
search_form_submit.click()
#br.close()
#sys.exit(0)
url=r"http://erp.bitmesra.ac.in/Academic/iitmsPFkXjz+EbtRodaXHXaPVt3dlW3oTGB+3i1YZ7alodHeRzGm9eTr2C53AU6tMBXuOAm5RgR4bqtOVgfGG9isuhw==?enc=3Q2Y1k5BriJsFcxTY7ebQh0hExMANhAKSl1CmxvOF+Y="
br.get(url)



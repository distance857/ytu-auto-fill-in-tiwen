import json
from lib2to3.pgen2 import driver
from pydoc import classname
import re
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import pytesseract  # 用于图片转文字
#from urllib.request import urlretrieve

one_driver = webdriver.Edge()
one_driver.get(r'http://xsyqfk.ytu.edu.cn/Web/Account/ChooseType')
sleep(20)
cookies = one_driver.get_cookies()    # 获取cookies
f1 = open('cookie.txt', 'w')  # cookies存入文件JSON字符串
f1.write(json.dumps(cookies))
f1.close()

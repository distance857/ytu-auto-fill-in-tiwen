import json
from lib2to3.pgen2 import driver
from pydoc import classname
import random
import re
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
#from urllib.request import urlretrieve

one_driver = webdriver.Edge()

one_driver.get(r'http://xsyqfk.ytu.edu.cn/Web/Account/ChooseType')

student_box = one_driver.find_element(By.XPATH, '//*[@id="teacher"]/a').click()


f1 = open('cookie.txt')
cookie = f1.read()
cookie_list = json.loads(cookie)  # json读取cookies
for c in cookie_list:
    one_driver.add_cookie(c)  # 取出的cookie循环加入driver

one_driver.refresh()    # 刷新后页面显示已登录
if one_driver.find_element(By.XPATH, '//*[@id="platfrom1"]/a') is None:
    print('CK已过期，请重新获取')
    sys.exit(0)
one_driver.find_element(By.XPATH, '//*[@id="platfrom1"]/a').click()

# 当前时间
# 时
hour = time.localtime().tm_hour
one_driver.find_element(
    By.XPATH, f'//*[@id="form1"]/div[2]/div/div[2]/div[1]/div[3]/div[2]/select[1]/option[{hour+1}]').click()
# 分
minute = time.localtime().tm_min
one_driver.find_element(
    By.XPATH, f'//*[@id="form1"]/div[2]/div/div[2]/div[1]/div[3]/div[2]/select[2]/option[{minute+1}]').click()
# 体温
wendu_1 = one_driver.find_element(
    By.XPATH, '//*[@id="Temper1"]/option[4]').click()
wendu_2 = one_driver.find_element(
    By.XPATH, f'//*[@id="Temper2"]/option[{random.randint(1,7)}]').click()
print(f'时间：{hour}:{minute}')
# 提交
one_driver.find_element(By.XPATH, '//*[@id="SaveBtnDiv"]/div/button').click()
one_driver.find_element(
    By.XPATH, '//*[@id="layui-m-layer0"]/div[2]/div/div/div[2]/span').click()

#one_driver.close()
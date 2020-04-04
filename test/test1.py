from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("美国新型冠状病毒死亡人数")
driver.find_element_by_id("su").click()
sleep(3)
driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()

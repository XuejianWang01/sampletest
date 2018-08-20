#!/usr/local/bin/python
from selenium import webdriver  
from pyvirtualdisplay import Display
from time import sleep
display = Display(visible=0, size=(800, 800))  
display.start()  

#
outputdir = "/tmp"  
options = webdriver.ChromeOptions()  
options.binary_location = '/bin/google-chrome'  
service_log_path = "{}/chromedriver.download_tax_rates.log".format(outputdir)  
service_args = ['--verbose']  
driver = webdriver.Chrome('/bin/chromedriver',  
        chrome_options=options,
        service_args=service_args,
        service_log_path=service_log_path)

#open connection
# driver = webdriver.Chrome()
#open chrome to first page
driver.get('https://www.baidu.com')
sleep(2)
driver.find_element_by_id("kw").click()
driver.find_element_by_id("kw").send_keys('PwC')
driver.find_element_by_id("su").click() 
driver.close()  
display.stop()  

将msedgedriver.exe放在python.exe同目录下

driver_url为下载的msedgedriver.exe所在位置

Egde浏览器下载链接：
https://www.microsoft.com/zh-cn/edge?form=MI13F4&OCID=MI13F4

msedgedriver.exe下载链接：(看清版本号)
https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

实现代码
from selenium import webdriver						#使用selenium模块
driver_url = r"C:\Program Files (x86)\Microsoft\Edge Beta\Application\msedgedriver.exe"	#设置路径
browser = webdriver.Edge(executable_path=driver_url)				#打开浏览器:浏览器驱动
browser.get("http://www.baidu.com")						#打开网页
browser.find_element_by_xpath("想选中的元素").send_keys("想输入的内容")			#选中元素输入内容
browser.find_element_by_xpath("想选中的元素").click()				#选中按钮点击按钮

import time
time.sleep(2)								#等待

browser.maximize_window()							#窗口最大化

# 个人资料路径								#实现免登录 仅限chrome
user_data_dir = (r'--user-data-dir=C:\Users\Master\AppData\Local\Google\Chrome\User Data')
# 加载配置数据
option = webdriver.ChromeOptions()
option.add_argument(user_data_dir)
# 启动浏览器配置
driver = webdriver.Chrome(chrome_options=option, executable_path=r'C:\Users\Master\AppData\Local\Google\Chrome\Application\chromedriver.exe')
driver.get("http://www.52pojie.cn/")
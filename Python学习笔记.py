#replace()函数
#可以替换字符串中的函数，未指定次数则全部替换

#示例：
#清空指定字符串
a = 'ABABAB'
a.replace('AB', '')
a = ''

#判断字符串是否由重复字符组成
a = 'ABABAB'
if a.replace('AB', '') == ''
	print('是的')

#2023.7.31
————————————————————————————————————————————————————————————————
#split(str,num)函数
#可以按照指定分隔符分割字符串
#str为分割符，默认为空格，num为分割次数，默认为-1，即全部分割

#示例:
#分割指定字符串
a = 'i love python'
a.split()

输出:
['i', 'love', 'python']

#指定分割次数
a = 'i love python'
a.split(' '， 1)

输出:
['i', 'love python']

2023.8.4
————————————————————————————————————————————————————————————————
#upper(str)函数
#将函数中的字符串转换为全大写后返回字符串，不会修改原字符串

#示例：
a = 'ABcdEFg'

print(a.upper())

输出:
'ABCDEFG'

2023.8.4
————————————————————————————————————————————————————————————————
#当Python中出现TypeError: ‘builtin_function_or_method’ object is not subscriptable的时候：
#一般是将圆括号()写成方括号[]了

2023.8.4
————————————————————————————————————————————————————————————————
#如果在输出列表时不想要[]边框:
#print( ','.join(mylist))

2023.8.4
————————————————————————————————————————————————————————————————
#由于字典在python中处于无序状态，所以查找元素后返回下标的函数均无法使用！

2023.8.4
————————————————————————————————————————————————————————————————
#Python判断数字的几个函数：
isnumeric()
#可以判断出大部分形式的数字字符串

#示例：
'123'.isnumeric()
输出:
True

'一二三'.isnumeric()
True

'Ⅲ'.isnumeric()
输出:
True

————————————
isdigit()
#可以判断出部分形式的数字字符串

示例：
'123'.isdigit()
输出:
True

'①'.isdigit()
输出:
True

'一二三'isdigit()
输出:
False

————————————
isnumeric()
#仅能判断出阿拉伯形式的数字字符串

示例：
'123'.isnumeric()
输出:
True

'一二三'.isnumeric()
输出:
Flase

'①'.isnumeric()
输出:
Flase

2023.8.4
————————————————————————————————————————————————————————————————
#Python中没有C语言中的逻辑运算符|| && ！，取而代之的是or and not

2023.8.4
————————————————————————————————————————————————————————————————
#在Python中打印字典

示例:
#打印完整字典:
person = {'name': 'Bob', 'age': 28, 'gender': 'male'}
print(person)

输出:
{'name': 'Bob', 'age': 28, 'gender': 'male'}

#打印字典中的值:
person = {'name': 'Bob', 'age': 28, 'gender': 'male'}
print(person.values())

输出:
dict_values(['Bob', 28, 'male'])

#打印字典中的键:
person = {'name': 'Bob', 'age': 28, 'gender': 'male'}
print(person.values())

输出:
dict_keys(['name', 'age', 'gender'])

#打印完整字典中并且没有括号和引号:
person = {'name': 'Bob', 'age': 28, 'gender': 'male'}

for key, value in person.items():
    print(f"{key}: {value}")

输出:
name: Bob
age: 28
gender: male

2023.8.4
————————————————————————————————————————————————————————————————

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
import time

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# 初始化 Selenium WebDriver，这里使用 Chrome 浏览器，你需要下载对应的驱动程序
driver = webdriver.Chrome()

# 打开网页
driver.get("http://www.sse.com.cn/market/stockdata/dividends/dividend/")

# 等待页面加载完成，可以根据具体情况设置等待时间
driver.implicitly_wait(30)
# 等待页面加载完成
time.sleep(4)
for ttt in range(66):

# 获取网页内容
page_source = driver.page_source
# print(page_source)
# 解析 HTML 内容
soup = BeautifulSoup(page_source, 'html.parser')
# print(soup)
# 关闭浏览器
driver.quit()

# 提取表格中的所有行
rows = soup.find_all('tr')

# 提取每行中的数据并存储到列表中
data = []
for row in rows:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    data.append(cols)

# 将列表转换为数据框
df = pd.DataFrame(data, columns=['股票代码', '股票简称', '公司名称', '每股红利', '股权登记日', '除息日'])
print(df)
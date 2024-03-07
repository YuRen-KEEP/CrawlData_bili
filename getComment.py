from selenium import webdriver
import time
import re
from openpyxl import Workbook


# 获取全部视频url
def getUrl(driver, url):
    # 向driver提交目标url
    driver.get(url)
    # 根据xpath获取含有所有剧集url的ul
    ul = driver.find_elements_by_xpath("//*[@id='eplist_module']/div[2]/ul/li")
    # 存储每集url的列表
    urls = []
    for li in ul:
        # 根据xpath提取每集url并添加到urls列表
        urls.append(li.find_element_by_xpath("./a").get_attribute("href"))
    return urls

# 根据每集url获取当前剧集的全部评论信息
def getHtml(driver, part, url, commentList):
    # 向浏览器提交url
    driver.get(url)
    # divs = driver.find_elements_by_xpath("//*[@id='comment_module']/div[2]/div/div[4]/div[1]")
    time.sleep(0.5)
    # 模拟人行为使浏览器划到底端以保证评论持续加载
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(0.5)
    # 经过浏览，最高评论数是第一集，共1143条评论，所以此处设置了1200条上限，是够用的
    for i in range(1, 30):
        # 判断xpath路径是否存在，以此作为当前剧集评论的结束条件
        if(nodeExisits("//*[@id='comment_module']/div[2]/div/div[4]/div[" + str(i) + "]")):
            if(i%20 == 0):
                # 模拟人行为使浏览器划到底端以保证评论持续加载
                driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                # 保持每20条评论输出一次提示信息，以便即使纠正错误
                print("第" + str(i) + "条评论读取完毕")
                time.sleep(0.5)
            # 获取每条评论的div块
            user = driver.find_element_by_xpath("//*[@id='comment_module']/div[2]/div/div[4]/div[" + str(i) + "]")
            # 分别根据xpath获取当前评论用户id、用户姓名、用户等级、评论内容、评论时间、评论点赞数
            id = user.get_attribute("data-id")
            name = user.find_element_by_xpath("./div[2]/div[1]/a[1]").text
            not_level = user.find_element_by_xpath("./div[2]/div[1]/a[3]/img").get_attribute("src")
            level = re.findall(r'.*level_(.+?).*svg', not_level)[0]
            comment = user.find_element_by_xpath("./div[2]/p").text
            times = user.find_element_by_xpath("./div[2]/div[2]/span[1]/span").text
            like = user.find_element_by_xpath("./div[2]/div[2]/span[2]/span").text
            # 添加获取到的当前评论信息到commentList
            commentList.append([part, id, name, level, comment, times, like])
        else:
            break
    return commentList

# 判断xpath路径是否存在，以此作为当前剧集评论的结束条件
def nodeExisits(xpath):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False

# 持久化数据模块
def saveData(fileName, commentList):
    # 创建一个Workbook对象，打开工作表
    wb = Workbook()
    ws = wb.active
    # 写入第一行数据作为每列数据信息内容
    ws.append(['剧集', 'bili_id', '昵称', '会员等级', '评论内容', '评论时间', '评论获赞'])
    # 分别从commentList中获取每条评论的信息并录入表格
    for item in commentList:
        ws.append(item)
    #保存
    wb.save(fileName)


if __name__ == '__main__':
    # 每集视频url列表
    urls = []
    # 评论信息存储列表
    commentList = []
    # 保存到本地的文件夹
    fileName = 'B站《决胜荒野》评论1.xlsx'

    driver = webdriver.Chrome() # 打开 chrome 浏览器

    # # 防止自动关闭浏览器
    # option = webdriver.ChromeOptions()
    # option.add_experimental_option("detach", True)
    # driver = webdriver.Chrome(chrome_options=option) # 将option作为参数添加到Chrome中

    # 视频首页
    url = f'https://www.bilibili.com/bangumi/play/ep702983'
    # 获取每一集视频的url
    urls = getUrl(driver, url)
    print(urls)
    # 记录视频的集数
    part = 1
    for url in urls:
        # 根据前边获取到的每一集url分别获取每一集评论
        getHtml(driver, part, url, commentList)
        part += 1
    # 保存爬取的内容到本地
    saveData(fileName, commentList)
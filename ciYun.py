import jieba
import os
import wordcloud
import pandas as pd
import matplotlib.pyplot as plt

# 选择目标xlsx文件并读取数据
fileName = 'B站《决胜荒野》评论.xlsx'
df = pd.read_excel(fileName, header=0)

# 清洗报错数据
text_arr = []
for comment in df['评论内容']:
    # 清洗数据，爬虫爬取数据时有些空评论在xlsx中类型为float，因此需要筛选出此部分数据
    if(type(comment) == float): continue
    text_arr.append(comment)

contents = ''.join(text_arr) # 将列表中所有文本合并

con_arr = jieba.lcut(contents)  # 文本分词后的列表
from  collections import Counter


def isun(x):
    # 此处为无用词、标点，生成词云中将剔除这些词
    unwords = ['，', ' ', '的', '、', '。', '了', '和', '#', '”', '“', '在', '日', '与', '等', '等', '中', '《', '》', '；', '新',
               '副', '以', '并', '/', '并', '）', '（', '上', '是', '及', '\xa0']
    return x not in unwords

new_words = filter(isun,con_arr)
# print(new_words)

con_num = Counter(new_words)

# 指定词云生成图形的参数，字体，图像大小，背景颜色等
word = wordcloud.WordCloud(font_path='./simhei.ttf',width=1000, height=500,background_color='white',collocations=False,max_font_size=120,max_words=2000)     #创建wordcloud对象
word.generate(contents)
# word.to_image()

# 保存词云到本地
word.to_file('图像.png')

# 展示词云
plt.imshow(word, interpolation='bilinear')
plt.axis("off")
plt.show()
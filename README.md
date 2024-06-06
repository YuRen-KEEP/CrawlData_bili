# 数据采集及可视化项目
## 项目概述
> 本程序旨在 爬取bilibili纪录片《决胜荒野第三季》（https://www.bilibili.com/bangumi/play/ep702983） 评论，并将评论用户、评论情况通过爬取数据可视化展示。对爬取到的数据进行多方面分析，决定进行以下方面的可视化展示：每集评论数量统计、每天评论数量统计、评论员会员等级分布、人均评论次数统计、评论字数情况统计、评论点赞情况统计（共计六张展示图）以及评论内容词云绘制
数据获取、解析主要使用selenium库（模拟人为操作获取网页数据），并使用了正则（re库）进行一部分数据的清洗，读写数据主要使用了（openpyxl库、pandas库），可视化展示为了实现交互式的体验，最终决定使用pandas_bokeh库，输出形式为.html形式以便交互式可视化的效果。词云部分主要使用了wordcloud库（字词处理）、matplotlib库（绘图）。

## 效果展示
![image](https://github.com/YuRen-KEEP/CrawlData_bili/assets/80758885/92441f2b-421b-44c0-a2cf-0740dc2ab388)
![image](https://github.com/YuRen-KEEP/CrawlData_bili/assets/80758885/27473029-1f6b-48bb-86da-dd91b97fcae7)
![image](https://github.com/YuRen-KEEP/CrawlData_bili/assets/80758885/00aa747a-79b7-4d83-8644-a3e4425c8d7c)
![image](https://github.com/YuRen-KEEP/CrawlData_bili/assets/80758885/2099bb56-d1d7-4c8b-932f-86d8a150f8c8)
![image](https://github.com/YuRen-KEEP/CrawlData_bili/assets/80758885/ce5a9f74-9361-4b38-a8b8-3f5585cb5266)
![image](https://github.com/YuRen-KEEP/CrawlData_bili/assets/80758885/89c2a089-7772-4751-a2d8-98d28ba9bacf)
![image](https://github.com/YuRen-KEEP/CrawlData_bili/assets/80758885/c170bfb5-bb66-495a-95c5-408126492b2e)

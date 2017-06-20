# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#定义需要爬取的数据
class TaobaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    #商品标题
    title = scrapy.Field()
    #商品链接
    link = scrapy.Field()
    #商品价格
    price = scrapy.Field()
    #评论总数
    comment_count = scrapy.Field()
    #商品销量
    sales = scrapy.Field()
    #商品产地
    location = scrapy.Field()
    #商品所在店铺名
    shopname = scrapy.Field()
    #快递费用
    kuaidi = scrapy.Field()
    #评论内容
    allrateContent = scrapy.Field()
    #评论人名称
    allUserNick = scrapy.Field()
    #评论时间
    allrateDate = scrapy.Field()
    #评论对象
    allauctionSku = scrapy.Field()
    pass

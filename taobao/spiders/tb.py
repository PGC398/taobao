from sys import path
import re,os
import urllib.request
import ssl
import scrapy
from sys import path
path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"../..")))
from scrapy.http import Request
from taobao.items import TaobaoItem
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.spiders import CrawlSpider, Rule

class TbSpider(RedisCrawlSpider):
    name = "tb"
    #allowed_domains = ["taobao.com"]
    redis_key = 'mycrawler:start_urls'
    start_urls = ['http://taobao.com/']

    def __init__(self, key=None,page=0, *args, **kwargs):
        super(TbSpider, self).__init__(*args, **kwargs)
        self.key=key
        self.page=int(page)
        
    def parse(self, response):
    	for i in range(0,self.page): #此处可以控制爬取该商品的页数，每页大约44件商品
    	    url = "https://s.taobao.com/search?q="+str(self.key)+"&search_type=item&s="+str(44*i)
    	    yield Request(url=url,callback=self.pages)

    def pages(self,response):
        body = response.body.decode("utf8","igrone")
        item = TaobaoItem()
        price = re.compile('"view_price":"(.*?)"').findall(body)
        title = re.compile('"raw_title":"(.*?)"').findall(body)
        comment_count = re.compile('"comment_count":"(.*?)"').findall(body)
        sales = re.compile('"view_sales":"(.*?)"').findall(body)
        location = re.compile('"item_loc":"(.*?)"').findall(body)
        kuaidi = re.compile('"view_fee":"(.*?)"').findall(body)
        shopname = re.compile('"nick":"(.*?)"').findall(body)
        isTmall = re.compile('"isTmall":(.*?),').findall(body)
        allitemid = re.compile('"nid":"(.*?)"').findall(body)
        allshopid = re.compile('"nid":"(.*?)"').findall(body)
        user_id = re.compile('"user_id":"(.*?)"').findall(body)

        for i in range(0,len(allitemid)):
            if isTmall[i]=='true':
                item["link"]="https://detail.tmall.com/item.htm?id="+str(allitemid[i])
                allrateContent=[]
                allUserNick=[]
                allrateDate=[]
                allauctionSku=[]
                for z in range(1,3):
                    url = "https://rate.tmall.com/list_detail_rate.htm?itemId="+str(allitemid[z])+"&sellerId="+str(user_id[z])+"&order=3&currentPage="+str(z)
                    body=urllib.request.urlopen(url).read().decode("gbk")
                    rateContent=re.compile('"rateContent":"(.*?)"').findall(body)
                    UserNick=re.compile('"displayUserNick":"(.*?)"').findall(body)
                    rateDate=re.compile('"rateDate":"(.*?)"').findall(body)
                    auctionSku=re.compile('"auctionSku":"(.*?)"').findall(body)
                    allrateContent.extend(rateContent)
                    allUserNick.extend(UserNick)
                    allrateDate.extend(rateDate)
                    allauctionSku.extend(auctionSku)
                

            else:
                item["link"]="https://item.taobao.com/item.htm?id="+str(allitemid[i])
                allrateContent=[]
                allUserNick=[]
                allrateDate=[]
                allauctionSku=[]
                for z in range(1,3):
                    url = "https://rate.taobao.com/feedRateList.htm?auctionNumId="+str(allitemid[z])+"&userNumId="+str(user_id[z])+"&currentPageNum="+str(z)+"&pageSize=20"
                    body=urllib.request.urlopen(url).read().decode("gbk")
                    rateContent=re.compile('":null,"content":"(.*?)"').findall(body)
                    UserNick=re.compile('"nick":"(.*?)"').findall(body)
                    rateDate=re.compile('"date":"(.*?)"').findall(body)
                    auctionSku=re.compile('"sku":"(.*?)"').findall(body)
                    allrateContent.extend(rateContent)
                    allUserNick.extend(UserNick)
                    allrateDate.extend(rateDate)
                    allauctionSku.extend(auctionSku)
                    
            item["allrateContent"]=allrateContent
            item["allUserNick"]=allUserNick
            item["allrateDate"]=allrateDate
            item["allauctionSku"]=allauctionSku


            item["price"]=price[i]
            item["title"]=title[i]
            item["comment_count"]=comment_count[i]
            item["sales"]=sales[i]
            item["shopname"]=shopname[i]
            item["location"] = location[i]
            item["kuaidi"] = kuaidi[i]
            
            yield item
        
#os.system('scrapy crawl tb')


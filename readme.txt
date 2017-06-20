�Ա�����
===
�Ա�scrapy����,������������ʵ��ָ����Ʒ���沢����Ʒ����������������⡣
����
===
	scrapy
	redis
	mongodb
ʹ��
===
	$ git clone ssh://git@42.123.127.93:10022/q851393199/taobao.git
	$ cd taobao
	$ python start.py

�ֲ�ʽ��������
===
��taobao/taobao/settings.py��
```python
# -*- coding: utf-8 -*-

SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# Ensure all spiders share same duplicates filter through redis.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# Scrapy settings for taobao project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'taobao'

SPIDER_MODULES = ['taobao.spiders']
NEWSPIDER_MODULE = 'taobao.spiders'


#��������
USER_AGENTS = [
	"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
	"Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
	"Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
	"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
	"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
	"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
	"Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
	"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
	"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

#����ip
PROXIES = [
	
	{'ip_port':'117.93.132.94:8998','user_pass':''},
	
]
# Obey robots.txt rules
ROBOTSTXT_OBEY = False


DOWNLOADER_MIDDLEWARES = {
#    'cnblogs.middlewares.MyCustomDownloaderMiddleware': 543,
    'taobao.middlewares.RandomUserAgent': 1, #���user agent
    #'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110, #������Ҫ�õ�
    #'taobao.middlewares.ProxyMiddleware': 100, #������Ҫ�õ�
}

ITEM_PIPELINES = {
    'taobao.pipelines.TaobaoPipeline': 300,
}


#�˴�����Mongodb���ݿ⣬���ڴ洢������ȡ����������
MONGODB_SERVER = "localhost" #�˴�����redis,������ʹ��127.0.0.1/localhost ����,�ӻ��ڴ˴���������ip��ַ,�����д洢�����ڷ�������
MONGODB_PORT = 27017   #�˿ں�
MONGODB_DB = "pipeline_db"  #���ݿ���
MONGODB_COLLECTION = "taobao"    #����

#�˴�����redis���ݿ⣬���ڴ洢��ȡ��url
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
REDIS_HOST = '127.0.0.1' #�˴�����redis,������ʹ�� 127.0.0.1/localhost ����,�ӻ��ڴ˴���������ip��ַ
REDIS_PORT= 6379
```

ע:������Ŀû��ʹ�ô���ip,��Ҫʹ��,ֻ���޸�taobao/taobao/settings.py��
```python
DOWNLOADER_MIDDLEWARES = {
#    'cnblogs.middlewares.MyCustomDownloaderMiddleware': 543,
    'taobao.middlewares.RandomUserAgent': 1, #���user agent
    #'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110, #������Ҫ�õ�
    #'taobao.middlewares.ProxyMiddleware': 100, #������Ҫ�õ�
}
```
�޸�Ϊ
```python
DOWNLOADER_MIDDLEWARES = {
#    'cnblogs.middlewares.MyCustomDownloaderMiddleware': 543,
    'taobao.middlewares.RandomUserAgent': 1, #���user agent
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110, #������Ҫ�õ�
    'taobao.middlewares.ProxyMiddleware': 100, #������Ҫ�õ�
}
```
����taobao/taobao/settings.py��
#����ip
```python
PROXIES = [
	
	{'ip_port':'117.93.132.94:8998','user_pass':''},
	
]
```
�м�����Ч����ip����
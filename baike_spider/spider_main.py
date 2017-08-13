from baike_spider import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()                #管理器
        self.downloader = html_downloader.HtmlDownloader()  #下载器
        self.parser = html_parser.HmtlParser()              #解析器
        self.outputer = html_outputer.HmtlOutputer()        #输出器

    def craw(self,root_url):                                #爬虫的调动程序
        count = 1                                           ### 记录当前爬取的url
        self.urls.add_new_url(root_url)                     #url管理器
        while self.urls.has_new_url():                     #启动爬虫循环
            try:
                new_url = self.urls.get_new_url()               #获取带爬虫的url
                print ("craw %d : %s"%(count,new_url))
                html_cont = self.downloader.download(new_url)   #启动下载器下载页面
                new_urls,new_data = self.parser.parse(new_url,html_cont)              #解析数据
                self.urls.add_new_urls(new_urls)                 #url补充进url管理器
                self.outputer.collect_data(new_data)             #收集数据

                if count == 1000:
                    break
                count = count + 1
            except:
                print ("craw failed")
        self.outputer.output_html()                          #输出收集好的数据



if __name__ == "__main__":
    root_url = 'https://baike.baidu.com/item/Python'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
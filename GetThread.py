# coding=utf8
__author__ = 'ives'

from BeautifulSoup import BeautifulSoup as bs
import os
import requests
import threading
import time

class GetThread (threading.Thread):

    url = "http://www.cnbeta.com/articles/%d.htm"
    agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"
    headers = {'User-Agent': agent}

    def __init__(self, i, s, e):
        threading.Thread.__init__(self)
        self.i = i
        self.s = s
        self.e = e

    def do(self):

        start = self.s
        end = self.e
        i = self.i

        print "[INFO] Thread %d starting: %d-%d" % (i, start, end)
        while start <= end:

            # if os.path.exists("./art/%d.txt" % start):
            #     print "[INFO][%d] Exist: %d" % (i, start)
            #     start += 2
            #     continue

            uri = self.url % start
            resp = requests.get(uri, allow_redirects=False, headers=self.headers)
            if resp.status_code != 200 and resp.status_code != 304:
                print "[ERROR][%d] Error Status Code %d -> %d: " % (i, start, resp.status_code)
                start += 2
                continue

            soup = bs(resp.content)
            title = soup.find(id="news_title").text.encode("utf8")
            date = soup.find(attrs={"class": "date"}).text.encode("utf8")
            introduction = soup.find(attrs={"class": "introduction"})
            ps = introduction.findAll("p")
            art = ""
            for p in ps:
                art += p.text
                art += u"\n"

            content = soup.find(attrs={"class": "content"})
            ps = content.findAll("p")
            for p in ps:
                art += p.text
                art += u"\n"

            f = open("./art/%d.txt" % start, "w")
            f.write(title + "\n")
            f.write(date + "\n")
            f.write(art.encode("utf8"))
            f.flush()
            f.close()

            print "[INFO][%d] ADD File: %s" % (i, f.name)

            start += 2
            time.sleep(1)

    def run(self):
        self.do()


#!coding=utf-8
"""
print Http Status Code of url in urlinfo 
"""

import threading
import urllib

urlinfo = ["http://www.sohu.com","http://www.baidu.com","http://www.sina.com"]

def open_url(url):
    temp = urllib.urlopen(url)
    print temp.getcode()
    temp.close()

if __name__ == "__main__":
    for i in xrange(len(urlinfo)):
        th = threading.Thread(target=open_url,args=[urlinfo[i]])
        th.start()
        th.join()
    print "thread end"

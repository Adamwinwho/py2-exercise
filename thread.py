#!coding=utf-8
"""
  create six threads,each thread print one num in info,and end with "the end"
"""

import threading

info = [1,2,3,4,55,232]

def print_num(num):
    print num

if __name__ == "__main__":
    for i in xrange(6):
        th = threading.Thread(target=print_num,args=[info[i]])
        th.start()
        th.join()
    print "the end"

# f = open("test.csv",'w')
# f.write("1,4,6,8,9")
# f.close()


#striping

# l = "       Hi        I        am         Aayan"
#
# k = l.strip()
#
# print(k)

# p = 11
# print(type(p))
#
# j = print(p)
#
# print(type(j))

#print always returnt none type obj
import os.path

import bs4
from bs4 import BeautifulSoup as bs
import requests
# slash = "\ "
# save_folder = "review"
# path = r'D:\flipkart_review_scraping'
#
# def mkdirc():
#     if not os.path.exists(save_folder):
#         os.makedirs(save_folder)
#         path = r'D:\flipkart_review_scraping'
#         return path + slash + save_folder.strip(" ")
#
# a = mkdirc()
# print(a)

# f = open("test.csv" , 'a')
# f.write("this")
# f.write("this")
# f.write("this")


l = ['hi this is mine, you are mine' , 'you have , no , writes' , 'T,A,L,K']

def replace_extra_comma(l):
    lf = []
    for i in range(len(l)):
        lf.append(l[i].replace(',' , " "))
    return lf
s = replace_extra_comma(l)
print(s)



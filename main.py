import os.path

import bs4
from bs4 import BeautifulSoup as bs
import requests
print("which product you want to search")
search = input()
search_str = search.strip()
def mksearch_url(search_str):
    initial_url = "https://www.flipkart.com/search?q="
    final_search_url = initial_url + search_str
    return final_search_url
#final_url = mksearch_url(search_str)
def mk_url_for_going_product_page(final_url):
    url_eliment = requests.get(final_url)
    get_content_of_url_eliment = url_eliment.content
    beautified_html_content = bs(get_content_of_url_eliment, 'html.parser')
    draft_link_for_go_product_page = \
    beautified_html_content.find_all("div", {'class': '_1AtVbE col-12-12'})[3].div.div.div.a['href']
    final_link_for_go_product_page = "https://www.flipkart.com" + draft_link_for_go_product_page
    return final_link_for_go_product_page

product_link = mk_url_for_going_product_page(mksearch_url(search_str))

def mk_bs_cont_for_find_tag(product_link):
    get_html_eliment = requests.get(product_link)
    html_content = get_html_eliment.content
    beautified_html_content = bs(html_content, 'html.parser')
    return beautified_html_content

beautified_html_content = mk_bs_cont_for_find_tag(product_link)

# slash = "\ "
# save_folder = "review"
# path = r'D:\flipkart_review_scraping'
#
# def mkdirc():
#     if not os.path.exists(save_folder):
#         os.makedirs(save_folder)
#         path = r'D:\flipkart_review_scraping'
#         return path + slash + save_folder.strip(" ")


#cust_name_func = beautified_html_content("div" , {"class":"row _3n8db9"})[0].div.p.text
cust_name = []

#cust_ratings_func = beautified_html_content("div" , {"class":"_3LWZlK _1BLPMq"})[0].text
cust_ratings = []

#cust_review_func = beautified_html_content("div" , {"class":"t-ZTKy"})[2].div.div.text
cust_review = []


for i in range(40):
    try:
        cust_name.append(beautified_html_content("div" , {"class":"row _3n8db9"})[i].div.p.text)
    except:
        pass
    try:
        cust_ratings.append(beautified_html_content("div", {"class": "_3LWZlK _1BLPMq"})[i].text)
    except:
        pass
    try:
        cust_review.append(beautified_html_content("div" , {"class":"t-ZTKy"})[i].div.div.text)
    except:
        pass

print(len(cust_review))
print(len(cust_name))
r = len(cust_ratings)

#in cust_review there is extra comma so it need to remove
custt_review = []
for i in range(r):
    add = cust_review[i].replace("," , "")
    custt_review.append(add)

print(len(custt_review))











file_name = search + "review" + ".csv"
f = open(file_name , 'a')
f.write("cust_name , cust_ratings , cust_review ")
f.write("\n")
for i in range(20):
    try:

        f.write(cust_name[i])
        f.write(", ")
    except:
        pass
    try:
        f.write(cust_ratings[i])
        f.write(", ")
    except:
        pass
    try:
        f.write(custt_review[i])
    except:
        pass
    try:
        f.write(",\n")
    except:
        pass






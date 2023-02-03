from bs4 import BeautifulSoup
import requests
from csv import writer


for i in range(1,21):
   url=f"https://www.amazon.in/gp/bestsellers/luggage/2917436031/ref=sr_bs_2_2917436031_{i}"

   page=requests.get(url)


   soup=BeautifulSoup(page.content,'html.parser')
   lists=soup.find_all('div',class_="zg-grid-general-faceout")
   Products_info=soup.find_all('a',class_='a-link-normal')
   with open('urls.csv','w',encoding='utf8',newline="")as f:
      thewriter=writer(f)
      header=['Product_url','ASIN','MANUFACTURER','PRODUCT_DESC']
      thewriter.writerow(header)
      for list in lists:
         Product_url=list.find('a',class_='a-link-normal').get("href")
         l=[]
         for i in lists:
              l.append(Product_url)
              for url1 in l:
                  x = "https://www.amazon.in/"
                  page1 = requests.get(x+url1)
                  print(page1)
                  soup_ = BeautifulSoup(page1.content, "html.parser")
                  lists_ = soup_.find_all('div',id="detailBullets_feature_div")
                  for list_ in lists_:
                      ASIN = list_.find('td', class_="a-size-base prodDetAttrValue").text.replace("\n", "")
                      MANUFACTURER = list_.find('span', class_="a-color-secondary a-size-base prodDetSectionEntry").text.replace("\n", "")

                      PRODUCT_DESC = list_.find('span', class_="a-list-item").text.replace("\n", "")
                      product_list = ['Product_url','ASIN','MANUFACTURER','PRODUCT_DESC']
                      print(product_list)
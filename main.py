from bs4 import BeautifulSoup
import requests
from csv import writer


for i in range(1,21):
   url=f"https://www.amazon.in/gp/bestsellers/luggage/2917436031/ref=sr_bs_2_2917436031_{i}"

   page=requests.get(url)


   soup=BeautifulSoup(page.content,'html.parser')
   lists=soup.find_all('div',class_="zg-grid-general-faceout")
   with open('product.csv','w',encoding='utf8',newline="")as p:
      thewriter=writer(p)
      header=['Product_url','Product_name','Number_of_Reviews','Ratings']
      thewriter.writerow(header)
      for list in lists:
         Product_url=list.find('a',class_='a-link-normal').get("href")
         Product_name=list.find('div',class_="_cDEzb_p13n-sc-css-line-clamp-3_g3dy1").text
         # Product_price = list.find('span', class_="a-size-base a-color-price")
         Number_of_Reviews = list.find('span', class_="a-size-small").text
         Ratings= list.find('span', class_="a-icon-alt").text
         Product_info=[Product_url,Product_name,Number_of_Reviews,Ratings]
         thewriter.writerow(Product_info)
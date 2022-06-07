from bs4 import BeautifulSoup
import requests,openpyxl


excel1 = openpyxl.Workbook()
sheet =excel1.active 
sheet.append(['Name','Price'])

source  = requests.get('https://healthybuddha.in/fruits-vegetables/fresh-fruits')
soup = BeautifulSoup(source.text ,'html.parser')


names = soup.find('div',id = "resp-banner-tab").find('div',class_="col-xs-12 p-b5 web-category-product-div").find('div',class_="tab-content col-lg-12").find('section',id="sidebar-main").find('div',id="content").find('div',id = "products").find('div',class_="products-block").find_all('div',class_="col-md-2 col-sm-6 text-center text-muted text-capitalize p0 product-col")



for name in names:
    
    fruitname = name.find('div').find('div',class_="product-meta resp-product-data").div.find('div',class_="left product-div-box").div.p.a.text  


    price = name.find('div').find('div',class_="product-meta resp-product-data").div.find('div',class_="right resp-product-right").find('div',class_="action resp-product-action").find('div').find('div').find('select').option.text
    print(price)
    break
    sheet.append([fruitname,price])





excel1.save("fruit-data1.xlsx")
    

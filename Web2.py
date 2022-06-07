
from bs4 import BeautifulSoup
import requests,openpyxl



excel = openpyxl.Workbook()
sheet =excel.active
sheet.append(['Name' , 'Price','Stock-left'])



source  = requests.get('https://communityfarm.in/product-category/fruits/')
soup = BeautifulSoup(source.text ,'html.parser')

name = soup.find('div',class_="communityFarm").find('div',class_="container-fluid").find('div',class_="mainRow").find('div',class_="content-area shop-page shop-has-sidebar").find('div',class_ = "row").find('div').find('div').find('div').find('div',class_="xlarge-10 large-9 columns").find_all('div',class_='row')



fruitlist = name[3].find('div').find('ul').find_all('li')



for fruit in fruitlist:
    fruitname = fruit.find('div').find('div',class_="productName").a.text
    price = fruit.find('div').find('form').find('div',class_="pricesGrids").find('div',class_="aligTxt float-left").span.bdi.text 
    stock = fruit.find('div').find('form').find('div',class_="pricesGrids").find('div',class_="aligTxt float-right").p.text
    sheet.append([fruitname , price,stock])
    



excel.save("fruits-data.xlsx")

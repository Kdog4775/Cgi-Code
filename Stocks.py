#dependencies
import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urlencode
import pandas as pd
import tkinter
import tkinter as tk

#Starting the gui
root = tk.Tk()

#list of URLs
urls = [
   'https://www.investing.com/equities/nike',
   'https://www.investing.com/equities/coca-cola-co',
   'https://www.investing.com/equities/microsoft-corp',
   'https://www.investing.com/crypto/bitcoin/btc-usd',
   'https://www.investing.com/crypto/ethereum/eth-usd',
   'https://www.investing.com/crypto/litecoin/ltc-usd'
]
  
#starting our CSV file
file = open('stockprices.csv', 'w')
writer = csv.writer(file)
writer.writerow(['Company', 'Price', 'Change'])
  
#looping through our list
for url in urls:
   #sending our request through the API
   params = {'api_key': 'ae8fe6738115c1cc0121c9498e967c1f', 'url': url}
   page = requests.get('http://api.scraperapi.com/', params=urlencode(params))
   #our parser
   soup = BeautifulSoup(page.text, 'html.parser')
   company = soup.find('h1', {'class': 'text-2xl font-semibold instrument-header_title__GTWDv mobile:mb-2'}).text
   price = soup.find('div', {'class': 'instrument-price_instrument-price__3uw25 flex items-end flex-wrap font-bold'}).find_all('span')[0].text
   change = soup.find('div', {'class': 'instrument-price_instrument-price__3uw25 flex items-end flex-wrap font-bold'}).find_all('span')[2].text
   #printing to have some visual feedback
   print('Loading :', url)
   print(company, price, change)
   #writing the data into our CSV file
   writer.writerow([company.encode('utf-8'), price.encode('utf-8'), change.encode('utf-8')])

#printing the data it collected 

file.close()


data= pd.read_csv("stockprices.csv")
data
data.columns
data.Company
data.Price
data.Change


#naming the gui window

#Showing the data from the csv
w = tk.Label(root, text=(data))


w.pack()
root.mainloop()

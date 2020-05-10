#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Extra Credit Assignment
#Beatiful soup to check worldometers.info for live Covid 19 Cases and Deaths across the world
#This program is to scrap number of people recovered, not recovered, and deaths across the USA and the world
import pandas as pd # Read CSV File
from bs4 import BeautifulSoup #Import beatiful soup library
import requests # Bring URL requests
import re # Regular Expressions
import csv #write and save to csv file

#create a function to save the covid 19 data to csv file
#the file is saved in covid19.csv
def save_csv(list_rows):
    try:
        print('\nSaving the results to CSV')
        with open('covid19.csv', 'a',  newline='', encoding='utf-8') as covidfile:
            writer = csv.writer(covidfile)
            writer.writerow(list_rows)
            print("outputs are saved successully")
    except PermissionError:
        print("covid19.csv is closed \n")
        
# First Define Main Function
def main(): 
    # bring in URL for COVID-19
    url = "https://www.worldometers.info/coronavirus/country/us"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "lxml") # Parse LXML File
    bsObj = BeautifulSoup(req.text, "html.parser")
    data = bsObj.find_all("div",class_ = "maincounter-number")
    stitle=soup.title
    #print(soup.title)
   # all_tables=soup.find_all("table")
    #print(all_tables)
    title= soup.find('title').get_text()
    print(title)
    #fine=re.findall(r"<title>(.*)</title>",req)
    #for event in fine:
        #print(event)
    #title1= re.findall(r"<title>(.*)</title>",stitle)
    #print(stitle)
    print("Total Number of Covid19 USA Cases: ", data[0].text.strip())
    print("Total Number of Covid19 Deaths in USA : ", data[1].text.strip())
    print("Total Number of Covid19 Recovered in USA: ", data[2].text.strip())
    #url = 'https://www.worldometers.info/coronavirus/country/us/'
    #res = requests.get(url) #Bring in URL Request
    #soup = BeautifulSoup(res.content, "lxml") # Parse LXML File
    print (" ")
    #url to get world data
    url = "https://www.worldometers.info/coronavirus/"  
    reqall = requests.get(url)
    soup = BeautifulSoup(reqall.text, 'html.parser') 
    table = soup.find('table', attrs={'id': 'main_table_countries_today'})
    #get header of the csv file
    header = [col_name.text.rstrip('\n').strip() for col_name in table.select('thead th')]
    save_csv(header)
    #print(row.text.rstrip('\n').strip())
    print(header)
    #get the covid details into csv file
    for row in table.select('tbody tr'):
        tds = [td.get_text().rstrip('\n').strip() for td in  row.select('td')]
        save_csv(tds)
        #print(row.text.rstrip('\n').strip())
        print(tds)
  
   
    #df = pd.DataFrame(results,columns=['title', 'current price', 'shipping cost'])
    #print(soup)
    #print(soup.title)

if __name__ == "__main__":
    main()





# In[ ]:





import requests
from bs4 import BeautifulSoup
import csv

url= "https://www.worldometers.info/coronavirus/"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
#print(soup.prettify())
table = soup.find(id ='main_table_countries_today')



#Title_Row
list= ['Country','Total_Cases','New Cases','Total_Deaths','New Deaths','Total Recovered','Active Cases','Serios/Critical','Tot cases/1M Pop','Deaths/1M']
with open('coronavirus.csv', 'w', newline='') as csvfile:
    #writer.writerow(list)
    writer = csv.writer(csvfile)

    writer.writerow(list)
    for data in table.find_all('tbody'):
        rows = data.find_all('tr')
        for row in rows:
            data1 = row.find('td').text
            a= row.find_all('td')[1].text.replace(',','').strip()
            b= row.find_all('td')[2].text.replace(',','').strip()
            c= row.find_all('td')[3].text.replace(',','').strip()
            d= row.find_all('td')[4].text.replace(',','').strip()
            e= row.find_all('td')[5].text.replace(',','').strip()
            f= row.find_all('td')[6].text.replace(',','').strip()
            g= row.find_all('td')[7].text.replace(',','').strip()
            h= row.find_all('td')[8].text.replace(',','').strip()
            i= row.find_all('td')[9].text.replace(',','').strip()

            str = '['+data1+','+a+','+b+','+c+','+d+','+e+','+f+','+g+','+h+','+i+']'
            #print(str)
            writer = csv.writer(csvfile)
            
            writer.writerow([data1,a,b,c,d,e,f,g,h,i])

      

import requests
from bs4 import BeautifulSoup
import csv

headers = {
    "User-Agent": "ExampleWikiScraper/1.0 (https://githhub.com/emcombs23; emcombs.23.sv@gmail.com)",
}

page = requests.get('https://www.nfl.com/standings/league/2025/REG', headers = headers).text

soup = BeautifulSoup(page, 'html.parser')

table = soup.find('table')

allData = []

allData.append([])
head = table.find('thead')
headersRow = head.find('tr')


headers = headersRow.find_all('th')
for header in headers[:-2]:
  print(header.text.strip())
  allData[0].append(header.text.strip())

body = table.find('tbody')
rows = body.find_all('tr')

for row in rows:
  allData.append([])
  values = row.find_all('td')
  nameTag = values[0].find('div', attrs = {'class':'d3-o-club-fullname'})
  text = "".join(nameTag.find_all(string=True, recursive=False)).strip()
  allData[-1].append(text)
  print(text)
  for value in values[1:-2]:
    print(value.text.strip())
    allData[-1].append(value.text.strip())
  print()


with open("standings.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(allData)
import requests
from bs4 import BeautifulSoup
import csv

headers = {
    "User-Agent": "ExampleWikiScraper/1.0 (https://githhub.com/emcombs23; emcombs.23.sv@gmail.com)",
}

page = requests.get('https://www.foxsports.com/nfl/team-stats?category=defense&season=2024&seasonType=reg', headers = headers).text

soup = BeautifulSoup(page, 'html.parser')

tables = soup.find_all('table')

headers = tables[0].find_all('th')

data = []
data.append([])

for header in headers:
  print(header.text)
  data[0].append(header.text.strip())

rows = tables[1].find_all('tr')

for row in rows:
  data.append([])
  tds = row.find_all('td')
  for td in tds[1:]:
    #print(td.text.strip())
    data[-1].append(td.text.strip())


with open("defense.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
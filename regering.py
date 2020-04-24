from bs3 import BeautifulSoup
import requests
import matplotlib.pyplot as plt

raw_html = requests.get('https://nl.wikipedia.org/wiki/Regering-Jambon').text
html = BeautifulSoup(raw_html, 'html.parser')

leden = []
views = []
for a in html.select('table.wikitable tr td:nth-child(2)'):
    leden.append(a.text.replace(' ', '_').strip())

for lid in leden:
    r = requests.get("https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/nl.wikipedia/all-access/all-agents/{}/daily/20191001/2019103100".format(lid))
    data = r.json()
    count = 0
    for item in data['items']:
        count += item['views']
    views.append(count)
    #print("{}".format(lid.replace('_', ' ') + ' ' + str(count)))

plt.style.use('seaborn-poster')
plt.title('Wikipedia page visits in Oct.')
plt.xlabel('Flemish minister')
plt.ylabel('Visits')


#plt.annotate(xy=[0, 1], s=str(14000))
plt.bar(['Jambon', 'Crevits', 'Somers', 'Weyts', 'Demir', 'Beke', 'Diependaele', 'Peeters', 'Dalle'], views, color='#ffe615')

#fig = plt.figure(figsize=(12, 8))
plt.savefig('flemish_ministers')
plt.show()
plt.plot()

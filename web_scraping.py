

import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://wiki.ubuntuusers.de/pdftk/').read()

# Bs object
soup = bs.BeautifulSoup(sauce,'lxml') # lxml = parser

# Show html
# print(soup)

# Show title of doc
# print(soup.title.string)
# print(soup.title.string)

# Show paragraph texts
# for paragraph in soup.find_all('p'):
#     print(paragraph.text)

# Show text between
print(soup.get_text())

# Show all links
# for url in soup.find_all('a'):
#     print(url.get('href'))

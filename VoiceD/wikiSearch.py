import urllib
import urllib2
from bs4 import BeautifulSoup
import html2text

article= "Einstien"
article = urllib.quote(article)

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')] #wikipedia needs this

resource = opener.open("http://en.wikipedia.org/wiki/" + article)
data = resource.read()
resource.close()
soup = BeautifulSoup(data,"lxml")
s = soup.find('div',id="bodyContent").p
print(html2text.html2text(data))
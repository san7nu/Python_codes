from google import search,get_page
import urlparse

query="ABCD"
withWiki = query + " wiki"
url=""

for j in search(withWiki, tld="co.in", num=1, stop=1, pause=2):
	url = j
	break

print(url)
par = urlparse.parse_qs(urlparse.urlparse(url).query)
print(par['<p>'])
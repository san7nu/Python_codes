from exchangelib import DELEGATE, Account, Credentials, Configuration
from bs4 import BeautifulSoup
import pandas as pd

creds = Credentials(
    username='myusername@example.com',  # Or myusername@example.com for O365
    password='password_here'
)

config = Configuration(server='outlook.office365.com', credentials=creds)

account = Account(
primary_smtp_address="myusername@example.com",
autodiscover=False, 
config = config,
access_type=DELEGATE)

data = [["",""]]

for i,item in enumerate(account.sent.all().order_by('-datetime_received')[:10]):
	try:
		soup = BeautifulSoup(item.body,"lxml")
		txt = soup.get_text().split("-->")[1]
		req = txt.split("Subject")[1].split("\n",1)[1].split("From")[0]
		my_reply = txt.split("From:")[0]
		data.append([req, my_reply])
		
	except Exception:
		pass

df = pd.DataFrame(data,columns=['req','reply'])
df.to_pickle('req_replies.pickle')
print("DONE")
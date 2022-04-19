##Find a 'scrappable' cryptocurrencies website where you can scrape the top 5 cryptocurrencies 
# and display as a formatted output one currency at a time. The output should display the name of the currency, 
# the symbol (if applicable), the current price and % change in the last 24 hrs and corresponding price (based on % change)

#Furthermore, for Bitcoin and Ethereum, the program should alert you via text 
# if the value falls below $40,000 for BTC and $3,000 for ETH.

#Submit your GitHub URL which should contain all the files worked in class as well as the above.#

from pydoc import cli
from twilio.rest import Client

accountSID = 'ACef15c55ebfa8dfaead2003361bca8897'
authToken = '2583a718f3e976bc4ad8998ea14b5ac2'

client = Client(accountSID,authToken)

TwilioNumber = '+14235941953'
mycellphone ='+18063356987'

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://crypto.com/price'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')		

title = soup.title

print(title.text)

crypto_table = soup.find('table')
table_rows = crypto_table.findAll("tr")


for x in range(1,6):
    td = table_rows[x].findAll('td')

    ranking = td[1].text
    og_crypto_name =td[2].text
    size = len(og_crypto_name)
    crypto_name = og_crypto_name[:size -3]
    deeper = soup.findAll('div',class_='css-0')
    current_price=(deeper[x-1].text.replace(',',''))
    current_price = float(current_price.replace('$',''))

    percent_change24=(td[4].text.replace('+',''))
    percent_change24=float(td[4].text.replace('%',''))
   

    if percent_change24 >= 0:
        percent_change24= percent_change24/100
        previous_price = round(current_price-(current_price*percent_change24),2)
    else:
        percent_change24= percent_change24/100
        previous_price = round(current_price+(current_price*percent_change24),2)

    percent_change24= format(percent_change24,'.2%')

    print(crypto_name)
    if crypto_name == 'Bitcoin':
        print('₿')
        if current_price <= 40000:
            textmessage = client.messages.create( to= mycellphone, 
                            from_= TwilioNumber, body = "Bitcoin fell below $40,000")
    if crypto_name =='Ethereum':
        print('Ξ')
        if current_price <= 3000:
            textmessage = client.messages.create( to= mycellphone, 
                            from_= TwilioNumber, body = "Etherium fell below $3,000")       
    print(f'The current price is: ${current_price}')
    print(f'The percent change in the last 24 hrs is {percent_change24}')
    print(f'The previous price was: ${previous_price}')
    input()


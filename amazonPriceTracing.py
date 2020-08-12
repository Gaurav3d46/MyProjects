import requests
from bs4 import BeautifulSoup
import smtplib

URL='https://www.amazon.in/dp/B07T8QC296/ref=cm_sw_r_wa_apa_i_GxwoEb1G3YVD5'
headers={"User-Agent":'https://developers.whatismybrowser.com/useragents/parse/?analyse-my-user-agent=yes'}
def check_price():

    page=requests.get(URL,headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')
    title=soup.find(id='productTitle').get_text()
    price=soup.find(id='priceblock_ourprice').get_text()
    converted_price=str(price[2:9])

    print(title.strip())
    print(converted_price)
    if(converted_price<'460.0'):
        send_mail()

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('gaurav3d56@gmail.com','jdiydxaywxeclvzi')

    subject='price fell down'
    body='Check the amazon link\nPrice has fallen of your product\n' 'https://www.amazon.in/dp/B07T8QC296/ref=cm_sw_r_wa_apa_i_GxwoEb1G3YVD5'
    msg=f"Subject:{subject}\n\n{body}"

    server.sendmail(
        'gaurav3d56@gmail.com',
        'gaurav3d56@gmail.com',
        msg
    )
    print('Hey mail has been sent!!')

    server.quit()

check_price()
© 2020 GitHub, Inc.

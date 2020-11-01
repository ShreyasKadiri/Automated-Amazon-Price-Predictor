import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.in/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-Camera/dp/B07B43WPVK/ref=asc_df_B07B43WPVK/?tag=googleshopdes-21&linkCode=df0&hvadid=397009265704&hvpos=&hvnetw=g&hvrand=6315764818241121339&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9040223&hvtargid=pla-552735796258&psc=1&ext_vrnc=hi"


headers = {
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])
    if converted_price <= 1.800:
        send_mail()
    print(converted_price)
    print(title.strip())

    if converted_price < 1.800:
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('anilchaudhry', 'ecdcndcoje-23nfjdf')
    subject = "Price Of the product fell down"
    body = "Please check the new low price here: https://www.amazon.in/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-Camera/dp/B07B43WPVK/ref=asc_df_B07B43WPVK/?tag=googleshopdes-21&linkCode=df0&hvadid=397009265704&hvpos=&hvnetw=g&hvrand=6315764818241121339&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9040223&hvtargid=pla-552735796258&psc=1&ext_vrnc=hi"
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'anilchaudhry1994@gmail.com',
        'anilchaudhry1994@gmail.com',
        message
    )

    print("Hey email has been sent!")
    server.quit()


while(True):
    check_price()
    # Send a mail and then sleep for one day -> 86400 seconds and then repeat
    time.sleep(86400)

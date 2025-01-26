from bs4 import BeautifulSoup
import requests
import smtplib
import os
import re
from dotenv import load_dotenv

load_dotenv()

URL="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

header={
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
}

response=requests.get(URL, headers=header)
yc_web_page=response.text
#_______Geting_main_price_________________________
soup=BeautifulSoup(yc_web_page, "html.parser")
price=soup.find('span', class_='aok-offscreen')
price_text = price.getText().replace('$', '')
productTitle=soup.find('span', id="productTitle").getText().strip()
cleaned_text = re.sub(r'\s+', ' ', productTitle)
lst=price_text.split()
price_value = float(lst[0])

if price_value<100:
    print(soup.prettify())
    msg=f"Subject:Amazon Price Alert!\n \n{productTitle}is now {price_value}\n url->{URL}".encode("utf-8")
    print(msg)
    #_____________________Sending________________
    FROM_EMAIL =os.getenv("FROM")
    TO_EMAIL = os.getenv("TO")
    #secutiy -> App passwords
    PASSWORD = os.getenv("APP_PASSWORD")

    smtp= os.getenv("SMTP_ADDRESS")
    connection=smtplib.SMTP(smtp, 587)
    connection.starttls()
    connection.login(FROM_EMAIL, PASSWORD)
    connection.sendmail(FROM_EMAIL,
                        TO_EMAIL,
                        msg=f"Subject:Amazon Price Alert!\n\n{productTitle}is now {price_value}\n{URL}".encode("utf-8")
                        )
    print('sent')
    connection.close()
else:
    print("Today is not your day")

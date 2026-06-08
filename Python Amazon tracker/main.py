import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import smtplib

# ---------------- LOAD ENV ---------------- #

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")

# ---------------- SETTINGS ---------------- #

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1"
TARGET_PRICE = 100

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

# ---------------- SCRAPE AMAZON ---------------- #

response = requests.get(URL, headers=headers)
website_html = response.text

print("Status code:", response.status_code)

soup = BeautifulSoup(website_html, "html.parser")

# ---------------- GET TITLE ---------------- #

title_tag = soup.find(id="productTitle")
title = title_tag.get_text().strip() if title_tag else "No title found"

# ---------------- GET PRICE ---------------- #

price_tag = soup.find(class_="a-offscreen")

if price_tag:
    price_text = price_tag.get_text()
    price = float(price_text.replace("$", "").replace(",", ""))
else:
    print("Price not found (Amazon may have blocked request or HTML changed)")
    price = None

print(title)
print(price)

# ---------------- SEND EMAIL IF PRICE DROPS ---------------- #

if price and price < TARGET_PRICE:

    message = f"Subject:Amazon Price Alert!\n\n{title}\nNow: ${price}\nBuy here: {URL}"

    with smtplib.SMTP(SMTP_ADDRESS, 587) as connection:
        connection.starttls()
        connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs=EMAIL_ADDRESS,
            msg=message.encode("utf-8")
        )

    print("Email sent!")
else:
    print("Price too high or not available")
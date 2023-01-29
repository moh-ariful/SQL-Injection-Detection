import requests
import re


url = "https://django.my.id"

keywords = ["sql", "Syntax", "Error", "Drop", "Union", "Where", "Or"]

response = requests.get(url)

text = response.text

for keyword in keywords:
    if re.search(keyword, text):
        print("Website lemah terhadap SQL Injection")
        break

else:
    print("Website tidak terdeteksi lemah terhadap serangan SQL Injection")

import requests
import re

# URL website yang akan diperiksa
url = "https://django.my.id"

# Kata kunci yang akan dicari dalam respon website
keywords = ["SQL", "syntax", "error", "Drop", "Union", "Where", "Select"]

# Mengirim request GET ke website
response = requests.get(url)

# Mengambil teks dari respon
text = response.text

# Mencari kata kunci dalam teks respon
for keyword in keywords:
    if re.search(keyword, text):
        print("Website rentan terhadap SQL injection!")
        break
else:
    print("Website tidak terdeteksi rentan terhadap SQL injection.")


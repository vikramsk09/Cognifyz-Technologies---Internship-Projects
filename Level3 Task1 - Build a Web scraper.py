import requests
from bs4 import BeautifulSoup

# Requesting the website
URL = "https://www.bbc.com/news"
response = requests.get(URL)
print(f"The response code is: {response}")

# Parse the HTML Document
soup = BeautifulSoup(response.content, "html.parser")

# Extracting news headlines from HTML
headlines = soup.find_all("h2")

# Display the headlines
for head in headlines:
    print(head.text, "\n")


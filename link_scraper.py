import requests
from bs4 import BeautifulSoup

url = "https://www.smu.edu.in/smit"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

links = set()

for link in soup.find_all("a"):
    href = link.get("href")

    if href:
        links.add(href)

with open("data/all_links.txt", "w", encoding="utf-8") as f:
    for link in sorted(links):
        f.write(link + "\n")

print(f"Found {len(links)} links")
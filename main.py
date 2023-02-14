from bs4 import BeautifulSoup

with open("Sample.html", "r") as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, "lxml")
    header_tags = soup.find_all("h5")
    
    for header in header_tags:
        print(header.text)
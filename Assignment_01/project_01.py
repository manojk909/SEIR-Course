import sys
import requests
from bs4 import BeautifulSoup

def main():
    #sending HTTP request and extract HTML
    def http_req(url):
        headers = {"User-Agent" : "Mozilla/5.0"}
        res = requests.get(url, headers=headers)
        if res.status_code != 200:
            print("Page NOT accessible:", url)
            sys.exit(1)
        return res.text

    #extract title of the page.
    def urlTitle(html):
        soup = BeautifulSoup(html, "html.parser")
        if soup.title:
            return soup.title.get_text().strip()
        else:
            return "No title"

    #extract page text.
    def bodyText(html):
        soup = BeautifulSoup(html, "html.parser")
        if soup.body:
            return soup.body.get_text(" ", strip=True)
        else:
            return ""

    #storing all the links in list present in page.
    def urlLinks(html):
        soup = BeautifulSoup(html, "html.parser")
        links = []
        for a in soup.find_all("a"):
            h = a.get("href")
            if h:
                links.append(h)
        return links
    #taking a URL on the command line
    if len(sys.argv) != 2:
        print("Provide argument like : python fileName.py url")
        sys.exit(1)

    url = sys.argv[1]

    html = http_req(url)
    title = urlTitle(html)
    body = bodyText(html)
    links = urlLinks(html)

    print("\nPage Title:\n", title)
    print("\nPage Body:\n")
    print(body)          # This will show whole text from body.
    # print(body[:5000])  # use this to see limited body text.

    print("\nPage Links:")
    for l in links:
        print(l)

    # If we want to see only limited links, we can use this.
    # linkLimit = 25
    # count = 0
    # for l in links:
    #     print(l)
    #     count += 1
    #     if count == linkLimit:
    #         break



if __name__ == "__main__":
    main()
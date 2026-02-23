import sys
import requests
from bs4 import BeautifulSoup
import re

def main():
    #sending HTTP request and extract HTML
    def http_req(url):
        headers = {"User-Agent" : "Mozilla/5.0"}
        res = requests.get(url, headers=headers)
        if res.status_code != 200:
            print("Page NOT accessible:", url)
            sys.exit(1)
        return res.text

    #exctracting page text.
    def bodyText(html):
        soup = BeautifulSoup(html, "html.parser")
        if soup.body:
            return soup.body.get_text(" ", strip=True)
        else:
            return ""

    #count frequency of words from body text.
    def wordFreq(bodyText):
        bodyText = bodyText.lower()
        wordLst = re.findall(r'\b[a-z0-9]+\b', bodyText)
        freq = {}
        for wd in wordLst:
            if wd in freq:
                freq[wd] += 1
            else:
                freq[wd] = 1
        return freq


    #polynomial rolling hash function
    p = 53  #base
    m = 2 ** 64 #mod
    def polyHash(wd):     
        h = 0
        power = 1
        for i in wd:
            h = (h + ord(i) * power) % m   # wd[i] = ord(c)..(ASCII for letter i in a word)
            power = (power * p) % m
        return h

    #I have not fully understood the logic of building Simhash
    #and calculating common bits between two URLs yet.
    #I will study this concept in detail and complete this part later.
    # def buildSimhash(freqMap):
    #     for wd in freqMap:

    # def commonBits():



    #taking two URL on the command line
    if len(sys.argv) != 3:
        print("Provide arguments like : python fileName.py url1 url2")
        sys.exit(1)

    url1 = sys.argv[1]
    url2 = sys.argv[2]

    html1 = http_req(url1)
    html2 = http_req(url2)

    bodyText1 = bodyText(html1)
    bodyText2 = bodyText(html2)

    freq1 = wordFreq(bodyText1)
    freq2 = wordFreq(bodyText2)

    print("Frequency of every word from url1: \n")
    print(freq1)
    print()
    print("Frequency of every word from url2: \n")
    print(freq2)


    
if __name__ == "__main__":
    main()
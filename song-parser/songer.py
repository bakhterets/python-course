#!/usr/bin/python3
#-------------------------------------------#
#   Program by Ilia B.                      #
#                                           #
#   Version Date    Info                    #
#       1.0 2023    Python course           #
#                                           #
#-------------------------------------------#


import ssl
import csv
import re
import requests
from urllib3 import poolmanager
from lxml import etree
import lxml.html


class TLSAdapter(requests.adapters.HTTPAdapter):

    def init_poolmanager(self, connections, maxsize, block=False):
        """Create and initialize the urllib3 PoolManager."""
        ctx = ssl.create_default_context()
        ctx.set_ciphers('DEFAULT@SECLEVEL=1')
        self.poolmanager = poolmanager.PoolManager(
                num_pools=connections,
                maxsize=maxsize,
                block=block,
                ssl_version=ssl.PROTOCOL_TLS,
                ssl_context=ctx)
session = requests.session()
session.mount('https://', TLSAdapter())

def parse(url):
    try:
        api = session.get(url)
    except:
        return
    tree = lxml.html.document_fromstring(api.text)
    text_original_lxml = tree.xpath('//*[@id="click_area"]/div//*[@class="original"]/text()')
    text_translated_lxml = tree.xpath('//*[@id="click_area"]/div//*[@class="translate"]/text()')
    
    text_original = []
    text_translated = []

    for i in text_original_lxml:
        i = str(i)
        i = i.replace("\n","")
        text_original.append(i)

    for i in text_translated_lxml:
        i = str(i)
        i = i.replace("\n","") 
        text_translated.append(i)

    print(text_original)
    print(text_translated)

    song_name = filename(url) + ".csv"
#
    with open(song_name, "w", newline='') as csvfile:
        fieldnames = ['original', 'translated']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for original, translated in zip(text_original,text_translated):
            writer.writerow({'original' : original, 'translated' : translated})

    for original, translated in zip(text_original,text_translated):
        print(original)
        print(translated)
        print("\n")
            
def filename(url):
    result = re.search(r"(?:^.*\/)([^\/]+)(?:\.html)", url)
    song_name = result.group(1)
    return song_name

#def requestcheck(url):
#    response = session.get(url)
#    print(response)

def main():
    #requestcheck("https://www.amalgama-lab.com")
    #link = "https://www.amalgama-lab.com/songs/b/bring_me_the_horizon/ludens.html"
    parse("https://www.amalgama-lab.com/songs/b/bring_me_the_horizon/ludens.html")

if __name__ == "__main__":
    main()

import requests,jsonify,json
from bs4 import BeautifulSoup
import urlparse

def get_thumbs(url):
    result = requests.get(url)
    # print "GETTHUM"
    # print result
    return image(result,url)
# url = "https://www.walmart.com/ip/54649026"


def image(result,url):
    urls=[]
    
    soup = BeautifulSoup(result.text, "html.parser")
    # print soup.prettify()
    # This will look for a meta tag with the og:image property
    og_image = (soup.find('meta', property='og:image') or
                        soup.find('meta', attrs={'name': 'og:image'}))
    if og_image and og_image['content']:
        # print og_image['content']
        # print ''
        urls.append(og_image['content'])
    
    # This will look for a link tag with a rel attribute set to 'image_src'
    thumbnail_spec = soup.find('link', rel='image_src')
    if thumbnail_spec and thumbnail_spec['href']:
        # print thumbnail_spec['href']
        # print ''
        urls.append(thumbnail_spec['href'])
    
    image = """<img src="%s"><br />"""
    for img in soup.findAll("img", src=True):
    #   print image % urlparse.urljoin(url, img["src"])
    #   print ''
       if img["src"] not in urls:
            urls.append(img['src'])
    # print len(urls)
    # print [x.encode("utf-8") for x in urls]
    # print "thumbs Above"
    #return urls
    # print json.dumps(urls)

    
    for desc in soup.find_all("description"):
        d = BeautifulSoup(desc.text,"lxml")
        img = d.find("img")
        # print("Title = {}".format(desc.find_previous("title").text))
        img_text = img.get("title") or img.get("alt","") if img else ""
        # print("Decscription = {}\n" .format(d.find(text=True) + img_text))
    return json.dumps(urls)
    
    
import requests
import re

from .models import Artigo 

def webCrawler(page):
    dupe_list = []
    total_links = []
    
    r = requests.get(page)
    html = r.text.encode("utf8")
    search = re.findall(r'<a href=[\'"?](https[://\w\-._]+)', html.decode("utf8"))

    for link in search:        
        if link not in total_links:
            try:
                dupe_list.append()
            except:
                pass          
        
        url_label = link.split(".")[1]
        print(url_label)

        Artigo(
              url=link,
              titulo=url_label.replace('com/', '').replace('/', ' ')
              ).save()  
        
        total_links = link            
            
            # Considerei salvar em txt, mas é mais fácil simples manter em uma variável.
            # with open("links.txt", "a") as file:
            #     file.write(f'{link}\n')

    dupe_list.clear()
           
    return total_links

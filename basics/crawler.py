from urllib import request
import random

def get_words(url='https://sixty-north.com/c/t.txt'):
    with request.urlopen(url) as story:
        story_words=[]
        for line in story:
            for word in line.split():
                story_words.append(word)
    return story_words

def download_with_proxy_url(url='http://test.com/assets/frontend/images/logo.png'):
    proxy = request.ProxyHandler({'https': 'proxypac.si.xx.yy:8080'})
    opener = request.build_opener(proxy)
    request.install_opener(opener)
    x = random.randrange(1, 1000)
    request.urlretrieve(url, str(x) + ".jpg")


def fetch_data(url='https://perso.telecom-paristech.fr/eagan/class/igr204/data/factbook.csv'):
    response=request.urlopen(url)
    res_text=str(response.read());
    lines=res_text.split("\\n")
    dest_url=r'goog.csv'
    fw=open(dest_url,'w')
    for line in lines:
        fw.write(line+"\n")
    fw.close()

if __name__=='__main__':
    print(get_words())
    download_with_proxy_url()
    fetch_data
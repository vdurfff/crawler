import requests
from bs4 import BeautifulSoup


for start_num in range(0,250,25):
    url = 'https://movie.douban.com/top250?start=' + str(start_num) + '&filter='
    headers ={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79'
    }
    response = requests.get(url,headers=headers)
    # print(response.text)

    soup = BeautifulSoup(response.text,'html.parser')
    titles = soup.findAll('span',attrs={'class':'title'})
    for title in titles:
        if '/' not in title.string:
            start_num = start_num + 1
            print(start_num, ' ',title.string)
import requests
from bs4 import BeautifulSoup


def fetch(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    user_info = soup.find_all('div', attrs={'class' : 'stat'})
    counter = 0

    for info in user_info:
        counter += 1

        if(counter>=5 and counter<=7):
            continue

        print(info.contents[0].string," ",info.contents[1].string)

        if(counter==16):
            break


def main():
    fetch('https://www.codewars.com/users/fenster25')


if __name__ == '__main__':
    main()

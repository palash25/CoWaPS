import requests
from bs4 import BeautifulSoup


def url_builder():
    uname = raw_input("Enter user name: ")
    url = 'https://www.codewars.com/users/' + uname
    return url


def fetch(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    user_info = soup.find_all('div', attrs={'class': 'stat'})
    counter = 0
    
    if not user_info:
        print "Username not found!"

        while 1:
            ch = raw_input("Do you want to try again? (y/n): ")
            if ch in ['y', 'Y']:
                main()
                return
            elif ch in ['n', 'N']:
                return
            else:
                print "Invalid Choice!"

    for info in user_info:
        counter += 1

        if(counter >= 5 and counter <= 7):
            continue

        print(info.contents[0].string, " ", info.contents[1].string)

        if(counter == 16):
            break


def main():
    fetch(url_builder())


if __name__ == '__main__':
    main()

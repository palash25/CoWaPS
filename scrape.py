import sys
import requests
from bs4 import BeautifulSoup


def url_builder(username):
    url = 'https://www.codewars.com/users/' + username
    return url


def fetch(url):
    counter = 0
    r = requests.get(url)

    if r.status_code == 500:
        print("Username does not exist, exiting...")
        return

    soup = BeautifulSoup(r.content, 'html.parser')
    user_info = soup.find_all('div', attrs={'class': 'stat'})

    for info in user_info:
        counter += 1

        if(counter >= 5 and counter <= 7):
            continue

        print(info.contents[0].string, " ", info.contents[1].string)

        if(counter == 16):
            break


def main(argv):

    if len(argv) == 1:
        fetch(url_builder(argv[0]))
    elif len(argv) > 1:
        print("Too many arguments!")
        print("Pass a username as an argument.")
    else:
        print("No arguments provided!")
        print("Pass a username as an argument.")


if __name__ == '__main__':
    main(sys.argv[1:])

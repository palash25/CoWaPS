import sys
import requests
from bs4 import BeautifulSoup
import csv
from texttable import Texttable


def url_builder(username):
    url = 'https://www.codewars.com/users/' + username
    return url


def store(data):
    '''
    This Function stores the
    data in a csv file
    '''
    csv.register_dialect('Dialect', delimiter=chr(9), quoting=csv.QUOTE_NONE)
    File = open("user_info.csv", "a")
    with File:
            writer = csv.writer(File, dialect='Dialect')
            writer.writerow(data)
            File.close()


def fetch(url):
    '''
    This function fetches the
    info about the user
    '''
    counter = 0
    r = requests.get(url)

    if r.status_code == 500:
        print("Username does not exist, exiting...")
        return

    soup = BeautifulSoup(r.content, 'html.parser')
    user_info = soup.find_all('div', attrs={'class': 'stat'})

    t = Texttable()
    info_list = []
    data = ['Attributes', 'Values']
    info_list.append(data)

    for info in user_info:
        counter += 1

        if(counter >= 5 and counter <= 7):
            continue

        data = [info.contents[0].string, info.contents[1].string]
        info_list.append(data)
        store(data)

        if(counter == 16):
            break

    t.add_rows(info_list)
    print(t.draw())


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

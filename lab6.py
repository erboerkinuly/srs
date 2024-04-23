import requests
from bs4 import BeautifulSoup

def read(url):
    response = requests.get(url)
    return response.text

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    quotes = soup.find_all('div', class_='quote')
    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        print(f'Цитата: {text}\nАвтор: {author}\n')

def main():
    url = 'http://quotes.toscrape.com/'
    html = read(url)
    parse_html(html)

if __name__ == "__main__":
    main()


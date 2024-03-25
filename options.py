import requests
from bs4 import BeautifulSoup
import urllib3
from urllib.parse import unquote 
import http.client
import json
import ast

urllib3.disable_warnings()
http.client._MAXHEADERS = 1000


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
url = 'https://autospot.ru/brands/changan/uni_t/suv/offer/364806/?car=2541717'


def save_json(response, file='cars_data.json'):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(response, f, ensure_ascii=False)


def load_json(file='cars_data.json'):
    with open(file, 'r', encoding='utf-8') as f:
        text = json.load(f)
        return text
    

def get_json_options_data(url):
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        scripts = soup.find_all('script')
        jsontext = scripts[-1].text
        jsontext = jsontext.replace('&q;', '"')
        json_data = json.loads(jsontext)
        return json_data
    else:
        print(f'Request error: {response.status_code}')


def get_main_chars(json_data):
    for item in json_data:
        if 'main-characteristics' in item:
            chars = json_data[item]['body']
    json_chars = {}
    for char in chars:
        json_chars[char['title']] = char['value']
    return json_chars


def get_chars(json_data):
    for item in json_data:
        if 'all-characteristics' in item:
            chars = json_data[item]['body']
    json_chars = {}
    for char in chars:
        for item in char['list']:
            json_chars[item['name']] = item['value']
    return json_chars


def get_options(json_data):
    for item in json_data:
        if 'all-options-two-column' in item:
            options1 = json_data[item]['body']['columns'][0]
            options2 = json_data[item]['body']['columns'][1]
            options = options1 + options2
    json_options = {}
    for option in options:
        option_items = []
        option_name = (option['name'])
        for item in option['options']:
            option_items.append(item['name'])
        json_options[option_name] = option_items
    return json_options


# json_data = get_json_options_data(url)

# save_json(json_data, file='options.json')

json_data = load_json('options.json')

json_main_chars = get_main_chars(json_data)
json_all_chars = get_chars(json_data)

json_chars = dict(list(json_main_chars.items()) + list(json_all_chars.items()))

save_json(json_chars, file='chars.json')
print(json_chars)

json_options = get_options(json_data)
save_json(json_options, file='options_list.json')
print(json_options)
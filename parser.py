import json
import urllib3
from pprint import pprint
import http.client
import requests
import pandas
from bs4 import BeautifulSoup

urllib3.disable_warnings()
http.client._MAXHEADERS = 1000

import requests

cookies = {
    'uid': '65fa8db63be76c.11152874',
    'exp-17468': 'a',
    'exp-18798': 'b',
    'exp-21441': 'b',
    'exp-22766': 'b',
    'exp-19304': 'b',
    'exp-19890': 'a',
    'exp-20121': 'a',
    'exp-20277': 'b',
    'exp-20561': 'a',
    'exp-21205': 'a',
    'exp-21490': 'a',
    'exp-21582': 'b',
    'exp-22516': 'b',
    'exp-21313': 'a',
    'exp-22114': 'a',
    'exp-23446': 'a',
    'exp-22668': 'a',
    'exp-23409': 'a',
    'exp-23688': 'b',
    'exp-23806': 'b',
    'exp-24052': 'b',
    'exp-24210': 'a',
    'exp-23974': 'a',
    'exp-24341': 'b',
    'exp-24340': 'a',
    'exp-24726': 'b',
    'exp-24748': 'b',
    'exp-24772': 'a',
    'exp-25026': 'a',
    'exp-24971': 'b',
    'exp-24963': 'b',
    'exp-24369': 'b',
    'exp-24370': 'b',
    'exp-25151': 'b',
    'exp-25152': 'b',
    'exp-25345': 'b',
    'exp-25351': 'a',
    'exp-25725': 'b',
    'exp-25891': 'a',
    'exp-25754': 'b',
    'exp-25828': 'b',
    'exp-25786': 'a',
    'exp-26405': 'b',
    'exp-24282': 'b',
    'exp-24954': 'a',
    'exp-26387': 'b',
    'exp-26485': 'a',
    'exp-26461': 'a',
    'exp-26906': 'b',
    'exp-26905': 'a',
    'exp-26782': 'b',
    'exp-27319': 'b',
    'exp-26712': 'a',
    'exp-26989': 'b',
    'exp-27306': 'a',
    'exp-27601': 'b',
    'exp-27681': 'a',
    'exp-27677': 'a',
    'exp-27678': 'b',
    'exp-27304': 'b',
    'exp-26987': 'a',
    'exp-27395': 'b',
    'exp-27458': 'b',
    'exp-27445': 'a',
    'exp-27261': 'b',
    'exp-28148': 'b',
    'exp-28253': 'b',
    'exp-28219': 'b',
    'exp-28293': 'a',
    'exp-28488': 'b',
    'exp-28543': 'b',
    'exp-28541': 'b',
    'exp-28529-1': 'a',
    'exp-28529-2': 'a',
    'exp-27400': 'b',
    'exp-28811': 'a',
    'exp-28627': 'b',
    'exp-28644': 'a',
    'exp-29099': 'b',
    'exp-28220': 'a',
    'exp-28736': 'b',
    'exp-29159': 'b',
    'exp-27520': 'b',
    'exp-29270': 'a',
    'exp-29257': 'b',
    'exp-30044': 'a',
    'tmr_lvid': 'c34fb6275808837208df9c96203fb06e',
    'tmr_lvidTS': '1710919158075',
    '_ym_uid': '1710919161198572481',
    '_ym_d': '1710919161',
    'advcake_track_id': '661c66e6-1ae9-1fbf-35d9-bf257f5cfc3b',
    'advcake_session_id': '5ca1693e-a581-61a4-9926-de28f6aa93f4',
    '_gcl_au': '1.1.371607054.1710919169',
    '_gpVisits': '{"isFirstVisitDomain":true,"idContainer":"100025C4"}',
    'modal_geo_refinement_was_shown': '1',
    'r2UserId': '1710919496336687',
    'analytic_id': '1710919500508504',
    'to_was_announced': '1',
    'front_token': '%7B%22access_token%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpZCI6IjFhYTBkNDEwZTc0YWEzNjA2ZDM1ODZjNjNiODk5MzUxZTA0ODY3YjMiLCJqdGkiOiIxYWEwZDQxMGU3NGFhMzYwNmQzNTg2YzYzYjg5OTM1MWUwNDg2N2IzIiwiaXNzIjoiIiwiYXVkIjoiY2xpZW50LWxrIiwic3ViIjpudWxsLCJleHAiOjE3MTEzNTYzNTMsImlhdCI6MTcxMTI2OTk1MywidG9rZW5fdHlwZSI6ImJlYXJlciIsInNjb3BlIjoiY29tbW9uIn0.cYSiZrpEypdacVXUQ2WdcwScVMz9Q9BArplRcU5ZVAOXijq6uN0YWwqOg6odLJZFLO6r4P7nmE122i4GetD_T0d7YMSLC1SfMdIMv3rCdm9LgsHLNNwS5MP1FdMn56wyEele79Uep8c9aI31_PXqTKNdI8PhKVFiOfrkM-b5kf3Bl_H7fZtYSbhXCUH69QWG-jhgXnvPXq2mEDZoVqVRjjb7U6xXRHETBeX93LeGRIzNdNgG56m0d2bNJJUTxsFcCgjs0r_qn8BD7oK2vmxX-DKivSIYWCwr-IAoDRyxHqJv3IzOdN03iKGnTzQLDfQKuUlrFTnKKWCcyLM2-ZJ4pA%22%2C%22expires_in%22%3A86400%2C%22token_type%22%3A%22bearer%22%2C%22scope%22%3A%22common%22%2C%22refresh_token%22%3Anull%2C%22expires%22%3A1711356353214%7D',
    '_ym_isad': '1',
    '_gid': 'GA1.2.1518098937.1711270062',
    'visit_id': 'M7dX2de8lkGx4RQWbQ2VBsfZ',
    'api_session': 'c2968f8bb901af03fb8dff5148267817',
    '_ym_visorc': 'b',
    '_gat_gtag_UA_44074754_1': '1',
    'advcake_track_url': '%3D20240325rPu8KPn25uxrHKUNcjlrOxIIs%2FQWmT2dbt%2FWM8FC%2BWUnSQrD1wH9d9Yd3eTVS9l5llXDD6wYr%2FU2S%2Byze58UaAmcSllCQW8pNU5AZMEnYhtOxDEuOCwu0C%2BbimVoG1X2%2FV1ypI8tkVOFMw42ZlAP%2FssJtfJbRcsZI7wRNr%2BJPVoSALiHwkoAX1zQ94cefWz6vHyGgSPbiOLX0Au3hSc0N3qbZuWrTs2bYV6vvD0FiLBlGkYLLdsUBdXp%2FVcjweOqmKlq7efjTXOLSd5LnJEKowp9n2%2B0pDJRwV5kw5fX9WyMtS53Phb1ik9fZAkxjmq%2BVOslNqyBNqrrciGJrkpUIYNxOD003OtQWUePnnh912GAAQu2wvEw%2F5MpK8E%2FwBWFXoepEX6F3PCJ74jdcorZ0IOIQVYxwJP24rHcVMlzBTm5LQcDzrD%2BTfrX2Vs3CV5%2BUyrzjoyGl6w9rRuNa1imaf%2BXNO9xl8n2f%2FfVIPLUCOvQLI4FLDuNQ1E2FIF6lqRy7Y0sacg%2FkmjzR00UEaBMKP9jScOZtuxvWBoQp6cSD%2BRwGLNs5OC303xXrCmf8mxxxCgt6UCaRd8IzmIKBNsxQfI4zodSPTJV89kjzExjfLX8Lzqif9JUD8pkUvT%2B1iDTzbkz%2FF5UN8bt1qSCrZhupbeuakQsjugAt6jZbXCqzd5s5mDDfEG2p%2BQ%3D',
    'selectedLocations': '%7B%22region%22%3A%5B%5D%2C%22radius%22%3A0%2C%22is_used_exist%22%3Atrue%7D',
    '_gp100025C4': '{"hits":6,"vc":1,"ac":1,"a6":1}',
    '_ga_DCBC15T7P0': 'GS1.1.1711330334.10.1.1711330364.0.0.0',
    '_ga': 'GA1.1.645963350.1710919164',
    '_ga_CJGC5D23L4': 'GS1.1.1711330334.10.1.1711330365.0.0.0',
    '_csrf': 'Km3tRExTkVZuMRjTS3IsOiCiDb1qDseu',
    '_ga_LGKF4DW8MH': 'GS1.1.1711330334.10.1.1711330384.10.0.0',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpZCI6IjFhYTBkNDEwZTc0YWEzNjA2ZDM1ODZjNjNiODk5MzUxZTA0ODY3YjMiLCJqdGkiOiIxYWEwZDQxMGU3NGFhMzYwNmQzNTg2YzYzYjg5OTM1MWUwNDg2N2IzIiwiaXNzIjoiIiwiYXVkIjoiY2xpZW50LWxrIiwic3ViIjpudWxsLCJleHAiOjE3MTEzNTYzNTMsImlhdCI6MTcxMTI2OTk1MywidG9rZW5fdHlwZSI6ImJlYXJlciIsInNjb3BlIjoiY29tbW9uIn0.cYSiZrpEypdacVXUQ2WdcwScVMz9Q9BArplRcU5ZVAOXijq6uN0YWwqOg6odLJZFLO6r4P7nmE122i4GetD_T0d7YMSLC1SfMdIMv3rCdm9LgsHLNNwS5MP1FdMn56wyEele79Uep8c9aI31_PXqTKNdI8PhKVFiOfrkM-b5kf3Bl_H7fZtYSbhXCUH69QWG-jhgXnvPXq2mEDZoVqVRjjb7U6xXRHETBeX93LeGRIzNdNgG56m0d2bNJJUTxsFcCgjs0r_qn8BD7oK2vmxX-DKivSIYWCwr-IAoDRyxHqJv3IzOdN03iKGnTzQLDfQKuUlrFTnKKWCcyLM2-ZJ4pA',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'uid=65fa8db63be76c.11152874; exp-17468=a; exp-18798=b; exp-21441=b; exp-22766=b; exp-19304=b; exp-19890=a; exp-20121=a; exp-20277=b; exp-20561=a; exp-21205=a; exp-21490=a; exp-21582=b; exp-22516=b; exp-21313=a; exp-22114=a; exp-23446=a; exp-22668=a; exp-23409=a; exp-23688=b; exp-23806=b; exp-24052=b; exp-24210=a; exp-23974=a; exp-24341=b; exp-24340=a; exp-24726=b; exp-24748=b; exp-24772=a; exp-25026=a; exp-24971=b; exp-24963=b; exp-24369=b; exp-24370=b; exp-25151=b; exp-25152=b; exp-25345=b; exp-25351=a; exp-25725=b; exp-25891=a; exp-25754=b; exp-25828=b; exp-25786=a; exp-26405=b; exp-24282=b; exp-24954=a; exp-26387=b; exp-26485=a; exp-26461=a; exp-26906=b; exp-26905=a; exp-26782=b; exp-27319=b; exp-26712=a; exp-26989=b; exp-27306=a; exp-27601=b; exp-27681=a; exp-27677=a; exp-27678=b; exp-27304=b; exp-26987=a; exp-27395=b; exp-27458=b; exp-27445=a; exp-27261=b; exp-28148=b; exp-28253=b; exp-28219=b; exp-28293=a; exp-28488=b; exp-28543=b; exp-28541=b; exp-28529-1=a; exp-28529-2=a; exp-27400=b; exp-28811=a; exp-28627=b; exp-28644=a; exp-29099=b; exp-28220=a; exp-28736=b; exp-29159=b; exp-27520=b; exp-29270=a; exp-29257=b; exp-30044=a; tmr_lvid=c34fb6275808837208df9c96203fb06e; tmr_lvidTS=1710919158075; _ym_uid=1710919161198572481; _ym_d=1710919161; advcake_track_id=661c66e6-1ae9-1fbf-35d9-bf257f5cfc3b; advcake_session_id=5ca1693e-a581-61a4-9926-de28f6aa93f4; _gcl_au=1.1.371607054.1710919169; _gpVisits={"isFirstVisitDomain":true,"idContainer":"100025C4"}; modal_geo_refinement_was_shown=1; r2UserId=1710919496336687; analytic_id=1710919500508504; to_was_announced=1; front_token=%7B%22access_token%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpZCI6IjFhYTBkNDEwZTc0YWEzNjA2ZDM1ODZjNjNiODk5MzUxZTA0ODY3YjMiLCJqdGkiOiIxYWEwZDQxMGU3NGFhMzYwNmQzNTg2YzYzYjg5OTM1MWUwNDg2N2IzIiwiaXNzIjoiIiwiYXVkIjoiY2xpZW50LWxrIiwic3ViIjpudWxsLCJleHAiOjE3MTEzNTYzNTMsImlhdCI6MTcxMTI2OTk1MywidG9rZW5fdHlwZSI6ImJlYXJlciIsInNjb3BlIjoiY29tbW9uIn0.cYSiZrpEypdacVXUQ2WdcwScVMz9Q9BArplRcU5ZVAOXijq6uN0YWwqOg6odLJZFLO6r4P7nmE122i4GetD_T0d7YMSLC1SfMdIMv3rCdm9LgsHLNNwS5MP1FdMn56wyEele79Uep8c9aI31_PXqTKNdI8PhKVFiOfrkM-b5kf3Bl_H7fZtYSbhXCUH69QWG-jhgXnvPXq2mEDZoVqVRjjb7U6xXRHETBeX93LeGRIzNdNgG56m0d2bNJJUTxsFcCgjs0r_qn8BD7oK2vmxX-DKivSIYWCwr-IAoDRyxHqJv3IzOdN03iKGnTzQLDfQKuUlrFTnKKWCcyLM2-ZJ4pA%22%2C%22expires_in%22%3A86400%2C%22token_type%22%3A%22bearer%22%2C%22scope%22%3A%22common%22%2C%22refresh_token%22%3Anull%2C%22expires%22%3A1711356353214%7D; _ym_isad=1; _gid=GA1.2.1518098937.1711270062; visit_id=M7dX2de8lkGx4RQWbQ2VBsfZ; api_session=c2968f8bb901af03fb8dff5148267817; _ym_visorc=b; _gat_gtag_UA_44074754_1=1; advcake_track_url=%3D20240325rPu8KPn25uxrHKUNcjlrOxIIs%2FQWmT2dbt%2FWM8FC%2BWUnSQrD1wH9d9Yd3eTVS9l5llXDD6wYr%2FU2S%2Byze58UaAmcSllCQW8pNU5AZMEnYhtOxDEuOCwu0C%2BbimVoG1X2%2FV1ypI8tkVOFMw42ZlAP%2FssJtfJbRcsZI7wRNr%2BJPVoSALiHwkoAX1zQ94cefWz6vHyGgSPbiOLX0Au3hSc0N3qbZuWrTs2bYV6vvD0FiLBlGkYLLdsUBdXp%2FVcjweOqmKlq7efjTXOLSd5LnJEKowp9n2%2B0pDJRwV5kw5fX9WyMtS53Phb1ik9fZAkxjmq%2BVOslNqyBNqrrciGJrkpUIYNxOD003OtQWUePnnh912GAAQu2wvEw%2F5MpK8E%2FwBWFXoepEX6F3PCJ74jdcorZ0IOIQVYxwJP24rHcVMlzBTm5LQcDzrD%2BTfrX2Vs3CV5%2BUyrzjoyGl6w9rRuNa1imaf%2BXNO9xl8n2f%2FfVIPLUCOvQLI4FLDuNQ1E2FIF6lqRy7Y0sacg%2FkmjzR00UEaBMKP9jScOZtuxvWBoQp6cSD%2BRwGLNs5OC303xXrCmf8mxxxCgt6UCaRd8IzmIKBNsxQfI4zodSPTJV89kjzExjfLX8Lzqif9JUD8pkUvT%2B1iDTzbkz%2FF5UN8bt1qSCrZhupbeuakQsjugAt6jZbXCqzd5s5mDDfEG2p%2BQ%3D; selectedLocations=%7B%22region%22%3A%5B%5D%2C%22radius%22%3A0%2C%22is_used_exist%22%3Atrue%7D; _gp100025C4={"hits":6,"vc":1,"ac":1,"a6":1}; _ga_DCBC15T7P0=GS1.1.1711330334.10.1.1711330364.0.0.0; _ga=GA1.1.645963350.1710919164; _ga_CJGC5D23L4=GS1.1.1711330334.10.1.1711330365.0.0.0; _csrf=Km3tRExTkVZuMRjTS3IsOiCiDb1qDseu; _ga_LGKF4DW8MH=GS1.1.1711330334.10.1.1711330384.10.0.0',
    'Origin': 'https://autospot.ru',
    'Referer': 'https://autospot.ru/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

def get_json_options_data(url):
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        scripts = soup.find_all('script')
        jsontext = scripts[-1].text
        jsontext = jsontext.replace('&q;', '"')
        try:
            json_data = json.loads(jsontext)
            return json_data
        except Exception as e:
            print(f'! ! ! Error loading json data: {e}')
            return False
    else:
        print(f'Request error: {response.status_code}')


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
            options = json_data[item]['body']['columns'][0]
    json_options = {}
    for option in options:
        option_items = []
        option_name = (option['name'])
        for item in option['options']:
            option_items.append(item['name'])
        json_options[option_name] = option_items
    return json_options



def get_json(page):
    params = {
        'sort': '-percent_discount',
        'limit': '1000',
        'page': page,
        'radius': '0',
        'picture_exp': '1',
    }
    try:
        response = requests.get(
            'https://api.autospot.ru/rest/filter/cars-with-parallel-import/',
            params=params,
            cookies=cookies,
            headers=headers,
            verify=False
        )
        return response.json()
    except:
        return None
    


def get_cars(json_data):
    cars = []
    items = json_data['items']
    for item in items:
        car = {}
        car['brand'] = item['brand_name']
        color = item['color_name']
        year = item['year']
        model = item['model_name']
        car['model_full'] = f"{car['brand']} {model}, {color}, {year}"
        car['city'] = item['city_name']
        car['image'] = item['slider'][0]['url']
        car['price'] = item['prices']['price']
        car['old_price'] = item['prices']['rrc_price']
        car['url'] = item['url']
        # car['body_type'] = item['body_type_name']
        # car['engine_type'] = item['engine_type']
        # car['engine_type_name_noun'] = item['engine_type_name_noun']
        # car['wheel_drive_name'] = item['wheel_drive_name']
        # car['transmission_type'] = item['transmission_type']
        # car['transmission_type_name_noun'] = item['transmission_type_name_noun']
        # car['engine_power'] = item['engine_power']
        cars.append(car)
    return cars



def save_json(response, file='cars_data.json'):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(response, f, ensure_ascii=False)


def load_json(file='cars_data.json'):
    with open(file, 'r', encoding='utf-8') as f:
        text = json.load(f)
        return text
    

def main():
    pages_count = 12
    count = 1
    all_cars = []
    all_cars_options_chars = []
    for page in range(1, pages_count + 1):
        json_data = get_json(page) 
        save_json(json_data)
        # json_data = load_json()
        if json_data:
            cars = get_cars(json_data)
            # save_json(cars, file='cars_data_out.json')
            print(page)
            for car in cars:
                car_options = {}
                # pprint(car, sort_dicts=False)
                print(f'{count}. {car["url"]}')
                json_options_data = get_json_options_data(car['url'])
                if json_options_data:
                    json_chars = get_chars(json_options_data)
                    json_options = get_options(json_options_data)
                    car_options[car['url']] = {
                        'Характеристики': json_chars,
                        'Опции': json_options
                    }
                    all_cars_options_chars.append(car_options)
                else:
                    print(f'Skiping: {car["url"]}')
                all_cars.append(car)
                count += 1


    print(count)
    save_json(all_cars,  file='cars_data_out.json')
    save_json(all_cars_options_chars,  file='cars_options_out.json')
    pandas.read_json("cars_data_out.json").to_excel("cars_data_out.xlsx")



if __name__ == '__main__':
    main()
import json
import urllib3
from pprint import pprint
import http.client
import requests
import pandas
from bs4 import BeautifulSoup
from multiprocessing.pool import ThreadPool as Pool

urllib3.disable_warnings()
http.client._MAXHEADERS = 1000

import requests

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
    '_gid': 'GA1.2.1518098937.1711270062',
    'api_session': 'c2968f8bb901af03fb8dff5148267817',
    'front_token': '%7B%22access_token%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpZCI6Ijk0YzQ0ZDBlMTQ3MmMyYWQ4YjZkNjVhM2YyZDEyNjhlMGIxYWI0N2MiLCJqdGkiOiI5NGM0NGQwZTE0NzJjMmFkOGI2ZDY1YTNmMmQxMjY4ZTBiMWFiNDdjIiwiaXNzIjoiIiwiYXVkIjoiY2xpZW50LWxrIiwic3ViIjpudWxsLCJleHAiOjE3MTE0NDUxNDQsImlhdCI6MTcxMTM1ODc0NCwidG9rZW5fdHlwZSI6ImJlYXJlciIsInNjb3BlIjoiY29tbW9uIn0.PdqRUuT09yLYMH9P0pEx8wrWtydnuVrrP5W2Bmo6IAwa8kPJD5obsBHimlVqaqUUJY4yIZeaVGx3sJ0jx9jBUGcxHFuxFguScRBnY4rCTtXvoakHcgrssui8ZSRmkI6A2y0_qhuGpPZBMNYZy6rCKsfhXL1voODyuHrstIddK5Mr-EjFVxzpduQaUhgDQwEx_qdGuOOzliM1T_G_7WuTsjdErnSDRy6lda3BDkxyalqmljajusLtycwxMyPrp31VhEf2I-8DxZVU2rRmcWilads1jN9q_HzLPoIclMY6_4Vs8eQ58c3rR_AOdDmmZPwN0lNtnMkIUcDU-Tm88PkAQA%22%2C%22expires_in%22%3A86400%2C%22token_type%22%3A%22bearer%22%2C%22scope%22%3A%22common%22%2C%22refresh_token%22%3Anull%2C%22expires%22%3A1711445144074%7D',
    '_ym_isad': '1',
    '_ym_visorc': 'b',
    'advcake_track_url': '%3D20240325T0sA30oDBsO0OVUlyqbdPJBoPx8EwoSIGhGxE5LbCvP18m%2FJNPIt%2FmV4%2Fm2dH4I7LklKtQMB9hY2jnKNdas4jLuBE7q2m%2BNkHg2LjrPWQw6cPGu207Z6imiBdTO9h2bEWGyNR4oQ98LFbDeg286FGpI4AnPaivYN72qyACnOj3aelCb1hTqCZvwm6JD55g0UuxqYXSeucAwSOBeAYGlYRiF0DWwV%2BPpk871Ond2dtTyub7v9qmrhKn7EWNZcbAEAEyoZrx7Ier3ZtYYaVFgLMmOxfFtw9Jgz4RxHcpn8WtgphV1NriUhgQZQZ24DqnViou8hg%2F6HVNC3DqGSsW%2FJE6poYoKFRnBMUaxyx6X0LLz0xREmqvRSWiFzPX4KgvrkAGXOBr8Kg7qAQwgElopTIhHPyUBPu%2FLy7Tem9pUmkFOg4c97neCwMU87FrvvM1rYFY4gHdMMRGzMWayjFZXadzfAoWnt86NBm9VAOPojYlCkX3qVrRioZecmo1YyNEucGM6rm%2Bp4xTbByUbkIrDbeH%2FE8cHs6fXKXxDowkQweJ6pZooNNV030Jh1QW5mFsOF%2B0a%2BeyegBYw39aeyo4umSBuVpRhzwWQIQE7GahzMfmpbv4dmZxmC0I9ueqbwbLg73P56uMR1CebMPmk%2Bj1j3o3X%2BURz%2Bjn7V1hvXtxNc21Or7dKolv6O2vg%3D',
    '_ga': 'GA1.1.645963350.1710919164',
    '_gp100025C4': '{"hits":10,"vc":1,"ac":1,"a6":1}',
    'selectedLocations': '%7B%22region%22%3A%5B%5D%2C%22radius%22%3A0%2C%22is_used_exist%22%3Atrue%7D',
    'visit_id': 'rwswGY9WC5xys1EGy9pfhi7M',
    '_ga_DCBC15T7P0': 'GS1.1.1711407418.14.1.1711409148.0.0.0',
    '_ga_CJGC5D23L4': 'GS1.1.1711407420.14.1.1711409148.0.0.0',
    '_ga_LGKF4DW8MH': 'GS1.1.1711407429.14.1.1711409148.60.0.0',
    '_csrf': 'PF0sYiQJf1nK9S5BsBv9hIIsp5cKTr0n',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpZCI6Ijk0YzQ0ZDBlMTQ3MmMyYWQ4YjZkNjVhM2YyZDEyNjhlMGIxYWI0N2MiLCJqdGkiOiI5NGM0NGQwZTE0NzJjMmFkOGI2ZDY1YTNmMmQxMjY4ZTBiMWFiNDdjIiwiaXNzIjoiIiwiYXVkIjoiY2xpZW50LWxrIiwic3ViIjpudWxsLCJleHAiOjE3MTE0NDUxNDQsImlhdCI6MTcxMTM1ODc0NCwidG9rZW5fdHlwZSI6ImJlYXJlciIsInNjb3BlIjoiY29tbW9uIn0.PdqRUuT09yLYMH9P0pEx8wrWtydnuVrrP5W2Bmo6IAwa8kPJD5obsBHimlVqaqUUJY4yIZeaVGx3sJ0jx9jBUGcxHFuxFguScRBnY4rCTtXvoakHcgrssui8ZSRmkI6A2y0_qhuGpPZBMNYZy6rCKsfhXL1voODyuHrstIddK5Mr-EjFVxzpduQaUhgDQwEx_qdGuOOzliM1T_G_7WuTsjdErnSDRy6lda3BDkxyalqmljajusLtycwxMyPrp31VhEf2I-8DxZVU2rRmcWilads1jN9q_HzLPoIclMY6_4Vs8eQ58c3rR_AOdDmmZPwN0lNtnMkIUcDU-Tm88PkAQA',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'uid=65fa8db63be76c.11152874; exp-17468=a; exp-18798=b; exp-21441=b; exp-22766=b; exp-19304=b; exp-19890=a; exp-20121=a; exp-20277=b; exp-20561=a; exp-21205=a; exp-21490=a; exp-21582=b; exp-22516=b; exp-21313=a; exp-22114=a; exp-23446=a; exp-22668=a; exp-23409=a; exp-23688=b; exp-23806=b; exp-24052=b; exp-24210=a; exp-23974=a; exp-24341=b; exp-24340=a; exp-24726=b; exp-24748=b; exp-24772=a; exp-25026=a; exp-24971=b; exp-24963=b; exp-24369=b; exp-24370=b; exp-25151=b; exp-25152=b; exp-25345=b; exp-25351=a; exp-25725=b; exp-25891=a; exp-25754=b; exp-25828=b; exp-25786=a; exp-26405=b; exp-24282=b; exp-24954=a; exp-26387=b; exp-26485=a; exp-26461=a; exp-26906=b; exp-26905=a; exp-26782=b; exp-27319=b; exp-26712=a; exp-26989=b; exp-27306=a; exp-27601=b; exp-27681=a; exp-27677=a; exp-27678=b; exp-27304=b; exp-26987=a; exp-27395=b; exp-27458=b; exp-27445=a; exp-27261=b; exp-28148=b; exp-28253=b; exp-28219=b; exp-28293=a; exp-28488=b; exp-28543=b; exp-28541=b; exp-28529-1=a; exp-28529-2=a; exp-27400=b; exp-28811=a; exp-28627=b; exp-28644=a; exp-29099=b; exp-28220=a; exp-28736=b; exp-29159=b; exp-27520=b; exp-29270=a; exp-29257=b; exp-30044=a; tmr_lvid=c34fb6275808837208df9c96203fb06e; tmr_lvidTS=1710919158075; _ym_uid=1710919161198572481; _ym_d=1710919161; advcake_track_id=661c66e6-1ae9-1fbf-35d9-bf257f5cfc3b; advcake_session_id=5ca1693e-a581-61a4-9926-de28f6aa93f4; _gcl_au=1.1.371607054.1710919169; _gpVisits={"isFirstVisitDomain":true,"idContainer":"100025C4"}; modal_geo_refinement_was_shown=1; r2UserId=1710919496336687; analytic_id=1710919500508504; to_was_announced=1; _gid=GA1.2.1518098937.1711270062; api_session=c2968f8bb901af03fb8dff5148267817; front_token=%7B%22access_token%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpZCI6Ijk0YzQ0ZDBlMTQ3MmMyYWQ4YjZkNjVhM2YyZDEyNjhlMGIxYWI0N2MiLCJqdGkiOiI5NGM0NGQwZTE0NzJjMmFkOGI2ZDY1YTNmMmQxMjY4ZTBiMWFiNDdjIiwiaXNzIjoiIiwiYXVkIjoiY2xpZW50LWxrIiwic3ViIjpudWxsLCJleHAiOjE3MTE0NDUxNDQsImlhdCI6MTcxMTM1ODc0NCwidG9rZW5fdHlwZSI6ImJlYXJlciIsInNjb3BlIjoiY29tbW9uIn0.PdqRUuT09yLYMH9P0pEx8wrWtydnuVrrP5W2Bmo6IAwa8kPJD5obsBHimlVqaqUUJY4yIZeaVGx3sJ0jx9jBUGcxHFuxFguScRBnY4rCTtXvoakHcgrssui8ZSRmkI6A2y0_qhuGpPZBMNYZy6rCKsfhXL1voODyuHrstIddK5Mr-EjFVxzpduQaUhgDQwEx_qdGuOOzliM1T_G_7WuTsjdErnSDRy6lda3BDkxyalqmljajusLtycwxMyPrp31VhEf2I-8DxZVU2rRmcWilads1jN9q_HzLPoIclMY6_4Vs8eQ58c3rR_AOdDmmZPwN0lNtnMkIUcDU-Tm88PkAQA%22%2C%22expires_in%22%3A86400%2C%22token_type%22%3A%22bearer%22%2C%22scope%22%3A%22common%22%2C%22refresh_token%22%3Anull%2C%22expires%22%3A1711445144074%7D; _ym_isad=1; _ym_visorc=b; advcake_track_url=%3D20240325T0sA30oDBsO0OVUlyqbdPJBoPx8EwoSIGhGxE5LbCvP18m%2FJNPIt%2FmV4%2Fm2dH4I7LklKtQMB9hY2jnKNdas4jLuBE7q2m%2BNkHg2LjrPWQw6cPGu207Z6imiBdTO9h2bEWGyNR4oQ98LFbDeg286FGpI4AnPaivYN72qyACnOj3aelCb1hTqCZvwm6JD55g0UuxqYXSeucAwSOBeAYGlYRiF0DWwV%2BPpk871Ond2dtTyub7v9qmrhKn7EWNZcbAEAEyoZrx7Ier3ZtYYaVFgLMmOxfFtw9Jgz4RxHcpn8WtgphV1NriUhgQZQZ24DqnViou8hg%2F6HVNC3DqGSsW%2FJE6poYoKFRnBMUaxyx6X0LLz0xREmqvRSWiFzPX4KgvrkAGXOBr8Kg7qAQwgElopTIhHPyUBPu%2FLy7Tem9pUmkFOg4c97neCwMU87FrvvM1rYFY4gHdMMRGzMWayjFZXadzfAoWnt86NBm9VAOPojYlCkX3qVrRioZecmo1YyNEucGM6rm%2Bp4xTbByUbkIrDbeH%2FE8cHs6fXKXxDowkQweJ6pZooNNV030Jh1QW5mFsOF%2B0a%2BeyegBYw39aeyo4umSBuVpRhzwWQIQE7GahzMfmpbv4dmZxmC0I9ueqbwbLg73P56uMR1CebMPmk%2Bj1j3o3X%2BURz%2Bjn7V1hvXtxNc21Or7dKolv6O2vg%3D; _ga=GA1.1.645963350.1710919164; _gp100025C4={"hits":10,"vc":1,"ac":1,"a6":1}; selectedLocations=%7B%22region%22%3A%5B%5D%2C%22radius%22%3A0%2C%22is_used_exist%22%3Atrue%7D; visit_id=rwswGY9WC5xys1EGy9pfhi7M; _ga_DCBC15T7P0=GS1.1.1711407418.14.1.1711409148.0.0.0; _ga_CJGC5D23L4=GS1.1.1711407420.14.1.1711409148.0.0.0; _ga_LGKF4DW8MH=GS1.1.1711407429.14.1.1711409148.60.0.0; _csrf=PF0sYiQJf1nK9S5BsBv9hIIsp5cKTr0n',
    'Origin': 'https://autospot.ru',
    'Referer': 'https://autospot.ru/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}


def get_json_options_data(url, car_options):
    # car_options = {}
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        scripts = soup.find_all('script')
        jsontext = scripts[-1].text
        jsontext = jsontext.replace('&q;', '"')
        try:
            json_options_data = json.loads(jsontext)
            if json_options_data:
                json_main_chars = get_main_chars(json_options_data)
                json_all_chars = get_chars(json_options_data)
                json_chars = dict(list(json_main_chars.items()) + list(json_all_chars.items()))
                json_options = get_options(json_options_data)
                car_options[url] = {
                    'Характеристики': json_chars,
                    'Опции': json_options
                }
            else:
                print(f'Skiping: {url}')
        except Exception as e:
            print(f'! ! ! Error loading json data: {e}')
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


def get_main_chars(json_data):
    for item in json_data:
        if 'main-characteristics' in item:
            chars = json_data[item]['body']
    json_chars = {}
    for char in chars:
        json_chars[char['title']] = char['value']
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


def get_json(page):
    params = {
        'sort': '-percent_discount',
        'limit': '500',
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
    pool_size = 50
    pages_count = 22
    # pages_count = 107
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
            print(f'Page: {page}')
            pool = Pool(pool_size)

            for car in cars:
                print(f'{count}. {car["url"]}')
                car_options = {}
                pool.apply_async(get_json_options_data, (car['url'], car_options))
                all_cars_options_chars.append(car_options)
                all_cars.append(car)
                count += 1
            pool.close()
            pool.join()

    print(count)
    save_json(all_cars,  file='cars_data_out.json')
    save_json(all_cars_options_chars,  file='cars_options_out.json')
    pandas.read_json("cars_data_out.json").to_excel("cars_data_out.xlsx")



if __name__ == '__main__':
    main()
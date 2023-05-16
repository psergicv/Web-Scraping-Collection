from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime, timedelta


def get_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-us,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "DNT": "1",
        "Connection": "keep-alive"
    }
    response = requests.get(url, headers=headers).text
    return response


def get_data(page):
    soup = BeautifulSoup(page, "lxml")

    daily_programs = soup.find_all("ul", class_="prg_list")

    epg = {}
    for prog_id, program in enumerate(daily_programs, start=1):
        epg[prog_id] = {}

        airing_time = program.find("div", class_="list_it").text
        epg[prog_id]["airing time"] = f"{airing_time[:2]}:{airing_time[2:]}"

        program_title = program.find('p').text.strip()
        epg[prog_id]["program title"] = program_title

        episode_number = program.find("div", class_="list_it").text.strip()
        epg[prog_id]["episode number"] = episode_number if episode_number else "n/a"
    return epg


def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)


def main():
    base_url = "https://www.ftv.com.tw/ProgList2020.aspx?day={}&ch=R"

    for i in range(6):  # 5 days ahead after the current day
        date = (datetime.now() + timedelta(days=i)).strftime("%m/%d/%Y")
        url = base_url.format(date)
        page = get_page(url)
        data = get_data(page)
        print(data)
        save_to_json(data, f'data_{date.replace("/", "_")}.json')


if __name__ == '__main__':
    main()

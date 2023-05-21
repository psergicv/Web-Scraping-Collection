from bs4 import BeautifulSoup
import requests
import json


def get_page(url):
    response = requests.get(url)
    return response.text


def get_data(page):
    soup = BeautifulSoup(page, "lxml")

    estate_card = soup.find_all("div", {"class": "status- views-row"})

    estate_data = []
    for card in estate_card:
        estate_id = card.find("div", {"class": "additional-info"}).find("span", {"class": "id"}).text[3:].strip()
        estate_title = card.find("div", {"class": "text"}).find("div", {"class": "views-field-title"}).find("a").text
        estate_price = card.find("div", {"class": "text"}).find("div", {"class": "wrapper-sides"}).find("div", {
            "class": "left-side-card"}).find("div", {"class": "price"}).text

        estate_data.append({
            'id': estate_id,
            'title': estate_title,
            'price': estate_price,
        })

    return estate_data


def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def main():
    url = "https://www.ataberkestate.com/turkey?field_property_status_target_id=1&field_property_type_target_id%5B%5D=41&field_property_type_target_id%5B%5D=42&field_property_type_target_id%5B%5D=43&term_node_tid_depth=All&field_rooms_target_id=All&field_price_value%5Bmin%5D=&field_price_value%5Bmax%5D=&field_id_value=&status_sold=1&sort_bef_combine=field_id_value+DESC&field_size_from_value%5Bmin%5D=&field_size_from_value%5Bmax%5D=&field_distance_sea_value%5Bmin%5D=&field_distance_sea_value%5Bmax%5D=&field_storeys_value%5Bmin%5D=&field_storeys_value%5Bmax%5D="
    page = get_page(url)
    data = get_data(page)
    save_to_json(data, 'data.json')


if __name__ == '__main__':
    main()

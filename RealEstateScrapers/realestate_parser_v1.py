from bs4 import BeautifulSoup
import requests


def get_page(url):
    response = requests.get(url)
    return response.text


def get_data(page):
    soup = BeautifulSoup(page, "lxml")
    return soup


def main():
    url = "https://www.ataberkestate.com/turkey?field_property_status_target_id=1&field_property_type_target_id%5B%5D=41&field_property_type_target_id%5B%5D=42&field_property_type_target_id%5B%5D=43&term_node_tid_depth=All&field_rooms_target_id=All&field_price_value%5Bmin%5D=&field_price_value%5Bmax%5D=&field_id_value=&status_sold=1&sort_bef_combine=field_id_value+DESC&field_size_from_value%5Bmin%5D=&field_size_from_value%5Bmax%5D=&field_distance_sea_value%5Bmin%5D=&field_distance_sea_value%5Bmax%5D=&field_storeys_value%5Bmin%5D=&field_storeys_value%5Bmax%5D="
    page = get_page(url)
    data = get_data(page)
    print(data)


if __name__ == '__main__':
    main()

from urllib.request import *
from urllib.parse import *


class CoordinateChanger():
    def __init__(self, base, lat, lng):
        # self.base = "https://www.finds.jp/ws/rgeocode.php?json"
        # self.lat = "34.7604130"
        # self.lng = "135.6269390"
        self.base = base
        self.lat = lat
        self.lng = lng

    def make_request_url(self, base, lat, lng):
        return "{}&lat={}&lon={}".format(base, lat, lng)

    def change_coordinate_to_city(self, base, lat, lng):
        url = self.make_request_url(base, lat, lng)
        response = urlopen(url)
        doc = response.read()
        return doc


if __name__ == "__main__":
    coordinateChanger = CoordinateChanger("https://www.finds.jp/ws/rgeocode.php?json", "34.7604130", "135.6269390")
    result = coordinateChanger.change_coordinate_to_city("https://www.finds.jp/ws/rgeocode.php?json", "34.7604130", "135.6269390")
    print(result)
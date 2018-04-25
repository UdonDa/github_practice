from urllib.request import *
from urllib.parse import *


class CoordinateChanger():
    def __init__(self, lat, lng):
        self.base = "https://www.finds.jp/ws/rgeocode.php?json"
        # self.lat = "34.7604130"
        # self.lng = "135.6269390"
        self.lat = lat
        self.lng = lng

    def make_request_url(self):
        return "{}&lat={}&lon={}".format(self.base, self.lat, self.lng)

    def send_request(self, url):
        response = urlopen(url)
        doc = response.read()
        return doc

    def change_coordinate_to_city(self):
        url = self.make_request_url()
        return self.send_request(url)

if __name__ == "__main__":
    coordinateChanger = CoordinateChanger("34.7604130", "135.6269390")
    result = coordinateChanger.change_coordinate_to_city()
    print(result)
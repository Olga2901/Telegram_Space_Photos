from dotenv import load_dotenv
import os
import requests
from datetime import datetime
from general_functions import download_image


def download_epic_photo_earth(nasa_token):
    payload = {
        "api_key": nasa_token,
    }
    epic_url = "https://api.nasa.gov/EPIC/api/natural/images"
    response = requests.get(epic_url, params = payload)
    response.raise_for_status()
    response_epic_url = response.json()
    for number, nasa_image in enumerate(response_epic_url):
        image = nasa_image["image"]
        epic_image = image.split("_")
        data_image = epic_image[2]
        data_format =  datetime.strptime(data_image, "%Y-%m-%d %H:%M:%S")
        part_image_url = "https://epic.gsfc.nasa.gov/archive/natural/"
        datetime_url = f"{part_image_url}/{data_format:%Y/%m/%d}/png/{image}.png"
        filepath = f"{epic_dir}/epic_earth_{number}.png"
        download_image(datetime_url, filepath)


def main():
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]
    epic_dir = "directory/epics_nasa/"
    download_epic_photo_earth(nasa_token)


if __name__ == "__main__":
    main()

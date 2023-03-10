import requests
import os
import shutil

API_KEY = os.getenv("NASAKEY")

base_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/"
rover = input()
url = base_url + rover + "/photos?"
date = input("DATE: ")

parameters = {
    "earth_date": date,
    "api_key": API_KEY
}

# curiosity works : 2015-6-3
# while spirt doesn't  

response = requests.get(url, params=parameters)
photo_list = response.json()['photos'] #! Handle non positive responses 
photos = []

if response.json()['photos'] == []:
    #TODO handle no photos
    pass 

for i in range(len(photo_list)):
    photos.append(photo_list[i]['img_src'])

for idx, image_url in enumerate(photos):
    res = requests.get(image_url, allow_redirects=True)
    if res.status_code == 200:
        with open(f"images/{idx}.png", "wb") as file:
            file.write(res.content)
        print(f"{idx} done")
    else:
        print(f"{idx} skipped")
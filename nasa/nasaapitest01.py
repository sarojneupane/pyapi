#!/usr/bin/python3

import requests

def main():
    roverresp = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=gT8fYoCsl1LkiFELTUe1kBKSPpMgxAVoVGwSmG6F").json()

    print(roverresp)
    cameraname = input("please input camera")
    for item in roverresp["photos"]:
        if item["camera"]["name"] == cameraname:
            print(item["rover"]["name"])
            print(item["earth_date"])
            print(f'item["img_src"] \n')

if __name__ == "__main__":
    main()

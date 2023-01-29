import config
import base64
import requests
import time
import pprint

def encode_file(file_name):
    with open(file_name, "rb") as file:
        return base64.b64encode(file.read()).decode("ascii")


def identify_plant(image):
    # More optional parameters: https://github.com/flowerchecker/Plant-id-API/wiki/Plant-identification
    params = {
        "images": [encode_file(image)],
        "latitude": 41.827630,
        "longitude": -71.402539,
        "datetime": round(time.time()),
        # Modifiers docs: https://github.com/flowerchecker/Plant-id-API/wiki/Modifiers
        "modifiers": ["crops_fast"],
        "plant_language": "en",
        # Plant details docs: https://github.com/flowerchecker/Plant-id-API/wiki/Plant-details
        "plant_details": ["common_names",
                          "edible_parts",
                          "name_authority"],
        }

    headers = {
        "Content-Type": "application/json",
        "Api-Key": config.PLANT_KEY
        }

    response = requests.post("https://api.plant.id/v2/identify",
                             json=params,
                             headers=headers)

    out = response.json()

    # find common name
    common_name = None
    for suggestion in out["suggestions"]:
        names = suggestion["plant_details"]["common_names"]
        if names:
            common_name = names[0]
            break

    if common_name == None:
        common_name = out["suggestions"][0]["plant_name"]



    return common_name

if __name__ == "__main__":
    print(identify_plant("images/1674958543.jpg"))

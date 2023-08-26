import time
import requests
import math
import random

TOKEN = "BBFF-JHt0XFKFoWd0te8Lz7HIaGOLxywJAa"  # Put your TOKEN here
DEVICE_LABEL = "rasberry-pi-4"  # Put your device label here 
VARIABLE_LABEL_1 = "download"  # Put your first variable label here
VARIABLE_LABEL_2 = "ping"
VARIABLE_LABEL_3 = "upload"


def build_payload(variable_1,variable_2,variable_3):
    # Creates two random values for sending data
    download_speed = int(random.randint(0 , 300))

    ping_speed = int(random.randint(0, 1000))

    upload_speed = int(random.randint(0, 300))
    
    payload = {variable_1: download_speed, variable_2: ping_speed, variable_3: upload_speed
               }

    return payload


def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    print(req.status_code, req.json())
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True


def main():
    payload = build_payload(
        VARIABLE_LABEL_1,
        VARIABLE_LABEL_2,
        VARIABLE_LABEL_3
    )

    print("[INFO] Attemping to send data")
    post_request(payload)
    print("[INFO] finished")


if __name__ == '__main__':
    while (True):
        main()
        time.sleep(1)
import hashlib
import random
import time
import uuid

import requests

PUBLIC_KEY = "a2ffa5c9be07488bbb04a3a47d3c5f6a"


def sha1(x: str):
    return hashlib.sha1(x.encode()).hexdigest()

def sha256(x: str):
    return hashlib.sha256(x.encode()).hexdigest()


def get_mac_address():
    as_hex = f"{uuid.getnode():012x}"
    return ":".join(as_hex[i : i + 2] for i in range(0, 12, 2))


def generate_nonce(miwifi_type=0):
    return f"{miwifi_type}_{get_mac_address()}_{int(time.time())}_{int(random.random() * 1000)}"


def generate_password_hash(nonce, password, newEncryptMode = 0):
    sha = sha1
    if newEncryptMode == 1:
        sha = sha256
    return sha(nonce + sha(password + PUBLIC_KEY))


class MiWiFi:
    def __init__(self, address="http://miwifi.com/", miwifi_type=0):
        if address.endswith("/"):
            address = address[:-1]

        self.address = address
        self.token = None
        self.miwifi_type = miwifi_type
        self.newEncryptMode = 0
        response = requests.get(
            f"{self.address}/cgi-bin/luci/api/xqsystem/init_info"
        ).json()
        if "newEncryptMode" in response:
            self.newEncryptMode = response["newEncryptMode"]

    def login(self, password):
        nonce = generate_nonce(self.miwifi_type)

        response = requests.post(
            f"{self.address}/cgi-bin/luci/api/xqsystem/login",
            data={
                "username": "admin",
                "logtype": "2",
                "password": generate_password_hash(nonce, password, self.newEncryptMode),
                "nonce": nonce,
            },
        )
        if response.status_code == 200:
            self.token = response.json()["token"]

        return response

    def logout(self):
        return requests.get(
            f"{self.address}/cgi-bin/luci/;stok={self.token}/web/logout"
        )

    def get_api_endpoint(self, endpoint):
        return requests.get(
            f"{self.address}/cgi-bin/luci/;stok={self.token}/api/{endpoint}"
        ).json()

    def post_api_endpoint(self, endpoint, data):
        return requests.post(
            f"{self.address}/cgi-bin/luci/;stok={self.token}/api/{endpoint}",
            data=data
        ).json()

    def status(self):
        return self.get_api_endpoint("misystem/status")

    def device_list(self):
        return self.get_api_endpoint("misystem/devicelist")

    def bandwidth_test(self):
        return self.get_api_endpoint("misystem/bandwidth_test")

    def pppoe_status(self):
        return self.get_api_endpoint("xqnetwork/pppoe_status")

    def wifi_detail_all(self):
        return self.get_api_endpoint("xqnetwork/wifi_detail_all")

    def country_code(self):
        return self.get_api_endpoint("xqsystem/country_code")

    def wan_info(self):
        return self.get_api_endpoint("xqsystem/wan_info")

    def check_wan_type(self):
        return self.get_api_endpoint("xqsystem/check_wan_type")

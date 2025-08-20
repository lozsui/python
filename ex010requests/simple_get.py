import requests

proxies = {
    "http": "secret",
    "https": "secret",
}


def get(url):
    try:
        response = requests.get(url, proxies=proxies, verify=False)
        response.raise_for_status()
        print("Status Code:", response.status_code)
        print("Response Body:")
        print(response.text)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)


def get_with_token(url):
    token = "token"

    params = {
        "arg1": "hello",
        "arg2": "world",
    }

    headers = {"accept": "application/xml", "Authorization": token}

    try:
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=10,
            verify=False,
            proxies=proxies,
        )
        response.raise_for_status()
        print("Status Code:", response.status_code)
        with open("out.xml", "w", encoding="utf-8") as f:
            f.write(response.text)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)


def get_token(url, user, pwd):
    payload = {"name": user, "password": pwd}

    try:
        response = requests.post(
            url, json=payload, timeout=10, verify=False, proxies=proxies
        )
        response.raise_for_status()
        print("Status Code:", response.status_code)
        print("Response JSON:", response.json())
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    get_with_token(url="https://example.com/api/foo")

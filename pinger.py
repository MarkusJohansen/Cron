import requests


def ping(targets: list):
    for target in targets:
        try:
            response = requests.get(target)
            print(f"{target} is up with status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"{target} is down with error {e}")


ping([
    "https://cv-nine-gilt.vercel.app/",
    "https://dagens-ord.vercel.app/"
])

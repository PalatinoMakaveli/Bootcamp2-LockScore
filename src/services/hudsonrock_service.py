import requests

URL = (
    "https://cavalier.hudsonrock.com/api/json/v2/"
    "osint-tools/search-by-email"
)


def check_email(email):

    response = requests.get(
        URL,
        params={"email": email},
        timeout=10
    )

    if response.status_code != 200:
        raise Exception("Erro ao consultar API")

    return response.json()
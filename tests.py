import requests

API_URL = "http://127.0.0.1:8000"


def test_get_index():
    response = requests.get(
        url=f"{API_URL}/"
    )

    assert response.status_code == 200, response.content


def test_post_mon_post():
    response = requests.post(
        url=f"{API_URL}/mon_post"
    )

    assert response.status_code == 200, response.content


def test_get_mon_get():
    response = requests.get(
        url=f"{API_URL}/mon_get"
    )

    assert response.status_code == 200, response.content
    data = response.json()

    assert data.get('status') == 1, data

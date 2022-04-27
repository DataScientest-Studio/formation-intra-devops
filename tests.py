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


def test_get_items():
    response = requests.get(
        url=f"{API_URL}/items"
    )

    assert response.status_code == 200, response.content
    data = response.json()

    assert len(data.get('items')) == 0, data


def test_get_health():
    response = requests.get(
        url=f"{API_URL}/health"
    )

    assert response.status_code == 200, response.content
    data = response.json()

    assert data.get('health') == "ok", data


def test_get_user():
    response = requests.get(
        url=f"{API_URL}/user"
    )

    assert response.status_code == 200, response.content
    data = response.json()

    assert data.get('name') == "paul", data


def test_get_bye():
    response = requests.get(
        url=f"{API_URL}/bye"
    )

    assert response.status_code == 200, response.content
    data = response.json()

    assert data.get('bye') == "bye", data

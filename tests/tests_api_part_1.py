import requests

host = 'https://reqres.in'


def test_register_success():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    response = requests.post(url=f'{host}/api/register', data=data)
    assert response.status_code == 200
    assert 'id' in response.json()
    assert 'token' in response.json()


def test_register_unsuccess():
    data = {
        "email": "sydney@fifen",
    }

    response = requests.post(url=f'{host}/api/register', data=data)
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'


def test_delete():
    response = requests.delete(url=f'{host}/api/users/2')
    assert response.status_code == 204
    assert response.text == ''


def test_single_user():
    response = requests.get(url=f'{host}/api/users/2')
    assert response.status_code == 200
    assert 'id' in response.json()['data']
    assert response.json()['data']['email'] == 'janet.weaver@reqres.in'
    assert response.json()['support']['url'] == 'https://reqres.in/#support-heading'


def test_single_user_not_found():
    response = requests.get(url=f'{host}/api/users/23')
    assert response.status_code == 404


def test_login_success():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.post(url=f'{host}/api/login', data=data)
    assert response.status_code == 200
    assert 'token' in response.json()


def test_login_unsuccess():
    data = {
        "email": "sydney@fifen",
    }

    response = requests.post(url=f'{host}/api/register', data=data)
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'


def test_resource_not_found():
    response = requests.get(url=f'{host}/api/unknown/23')
    assert response.status_code == 404
    assert response.text == '{}'


def test_requested_page_number():
    response = requests.get(
        "https://reqres.in/api/users", params={"page": 2}
    )

    assert response.status_code == 200
    assert response.json()["page"] == 2
    assert response.json()["total"] == 12


def test_users_list_default_lenght():
    response = requests.get("https://reqres.in/api/users")

    assert len(response.json()["data"]) == 6

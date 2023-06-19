from jsonschema.validators import validate
from helper import load_json_schema, reg_session


def test_register_success():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = reg_session.post(url=f'/api/register', data=data)

    validate(instance=response.json(), schema=load_json_schema('post_register_success.json'))


def test_register_unsuccess():
    data = {
        "email": "sydney@fifen",
    }

    response = reg_session.post(url='/api/register', data=data)
    validate(instance=response.json(), schema=load_json_schema('register_unsuccess.json'))


def test_single_user():
    response =reg_session.get(url='/api/users/2')

    validate(instance=response.json(), schema=load_json_schema('single_user.json'))


def test_list_resource():
    response = reg_session.get(url='/api/unknown')

    validate(instance=response.json(), schema=load_json_schema('list_resource.json'))


def test_login_success():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = reg_session.post(url='/api/login', data=data)

    validate(instance=response.json(), schema=load_json_schema('login_success.json'))


def test_login_unsuccess():
    data = {
        "email": "sydney@fifen",
    }
    response = reg_session.post(url='/api/register', data=data)

    validate(instance=response.json(), schema=load_json_schema('login_unsuccess.json'))


def test_list_users():
    response = reg_session.get(url='/api/users', params={"page": 2})

    validate(instance=response.json(), schema=load_json_schema('list_users.json'))


def test_single_resource():
    response = reg_session.get(url='/api/unknown/2')

    validate(instance=response.json(), schema=load_json_schema('single_resource.json'))


def test_user_create():
    data = {
        "name": "morpheus",
        "job": "leader"
    }
    response = reg_session.post(url='/api/users', data=data)

    validate(instance=response.json(), schema=load_json_schema('user_create.json'))


def test_user_update():
    data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = reg_session.put(url='/api/users/2', data=data)

    validate(instance=response.json(), schema=load_json_schema('user_update.json'))

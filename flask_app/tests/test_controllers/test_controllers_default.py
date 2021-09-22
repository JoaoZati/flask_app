import pytest

from flask_app import app


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def resp_home(client):
    resp_home = client.get('/')
    return resp_home


def test_home_index(resp_home):
    assert resp_home.status_code == 200


def test_titulo_home(resp_home):
    assert b"Bem Vindo ao Flask app!" in resp_home.data


@pytest.fixture(scope="function")
def user_mock(request):
    return request.param


@pytest.mark.parametrize(
    'user_mock',
    ['Joao', 'Guilherme']
)
def test_resp_usuario(client, user_mock):
    resp_usuario = client.get(f'/usuario/{user_mock}')
    assert resp_usuario.status_code == 302

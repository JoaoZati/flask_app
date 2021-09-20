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


@pytest.mark.parametrize(
    'name',
    ['joao', 'guilherme']
)
def test_titulo(resp_home, name):
    assert bytes(f"Bem Vindo {name}!", 'ascii') in resp_home.data


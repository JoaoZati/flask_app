import pytest

from flask_app import app


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def resp_login(client):
    resp_login = client.get('/login')
    return resp_login


def test_login_resp(resp_login):
    assert resp_login.status_code == 200


def test_titulo_login(resp_login):
    for word in [b'Login', b'Username', b'Password', b'Remember-me']:
        assert word in resp_login.data

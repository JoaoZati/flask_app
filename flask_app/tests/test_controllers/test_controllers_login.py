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

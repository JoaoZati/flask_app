import pytest

from flask_app import app
from flask_app.controllers.default import index


@pytest.fixture
def client():
    return app.test_client()


def test_index(client):
    resp = client.get('/')
    assert resp.status_code == 200



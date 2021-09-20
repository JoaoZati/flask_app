import pytest


@pytest.fixture
def numero():
    return 1


def test_int(numero):
    assert numero == 1

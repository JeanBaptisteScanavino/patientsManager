import pytest
from requests import request


def test_server_is_launched():
    response = request("GET", "http://0.0.0.0:8000/")
    assert response.status_code == 200

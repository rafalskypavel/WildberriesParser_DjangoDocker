from django.test import TestCase

import pytest
from django.test import Client


@pytest.fixture
def client():
    return Client()


def test_health(client):
    response = client.get("/api/v1/products/")
    assert response.json() == {"status": "ok"}
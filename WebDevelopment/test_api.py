import pytest
from requests import get, post
from json import loads

class TestAPI:
    def setup(self):
        self.url = "http://127.0.0.1:8000"

    def test_APIstatus(self):
        resp = get(self.url)
        assert resp.ok

    def test_APIresponse(self):
        resp = get(self.url)
        message = loads(resp.text)
        assert message == ["Bem vindo!"]

    def test_POSTmethod(self):
        resp = post(self.url + "/exapi", json={"valor1": 24, "valor2": 4, "operação": "MULTIPLICAÇÃO"})
        message = loads(resp.text)
        assert message == {'valor1': 24, 'valor2': 4, 'operação': 'MULTIPLICAÇÃO'}


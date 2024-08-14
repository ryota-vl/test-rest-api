import os
from requests import Session
from pytest import fixture


class BaseSession(Session):
    def __init__(self, base_url: str):
        super().__init__()
        self.base_url = base_url

    def request(self, method, url, *args, **kwargs):
        url = self.base_url + url
        return super().request(method, url, *args, **kwargs)


@fixture(scope='session')
def session():
    base_url = os.getenv('BASE_URL', 'https://jsonplaceholder.typicode.com/')
    session = BaseSession(base_url)

    # response = session.post('/posts', json={'title': 'foo', 'body': 'bar', 'userId': 1})
    # session.headers.update({'Authorization': f'Bearer {response.json()["id"]}'})

    yield session

    session.close()

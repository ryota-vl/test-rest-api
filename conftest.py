import os
from requests import Session
from pytest import fixture


class BaseSession(Session):
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url

    def request(self, method, url, **kwargs):
        if self.base_url and not url.startswith(('http://', 'https://')):
            url = f'{self.base_url.rstrip("/")}/{url.lstrip("/")}'
        return super().request(method, url, **kwargs)


@fixture(scope='session')
def session():
    base_url = os.getenv('BASE_URL', 'https://jsonplaceholder.typicode.com')
    session = BaseSession(base_url=base_url)

    # auth setup example
    # response = session.get('/users/1')
    # token = response.json().get('phone')
    # session.headers.update({'Authorization': f'Bearer {token}'})

    yield session

    session.close()

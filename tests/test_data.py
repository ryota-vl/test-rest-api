from pytest import mark


@mark.smoke
def test_posts(session):
    response = session.get('/posts')
    assert response.ok
    assert len(response.json()) == 100


def test_post_1(session):
    response = session.get('/posts/1')
    assert response.ok
    payload = response.json()
    assert payload['id'] == 1
    assert payload['title'] == 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'
    assert 'recusandae consequuntur expedita' in payload['body']


def test_post_100(session):
    response = session.get('/posts/100')
    assert response.ok
    payload = response.json()
    assert payload['id'] == 100
    assert payload['title'] == 'at nam consequatur ea labore ea harum'
    assert 'cupiditate quo est a modi' in payload['body']


@mark.smoke
def test_comments_post_1(session):
    response = session.get('/comments?postId=1')
    assert response.ok
    payload = response.json()
    assert len(payload) == 5


def test_headers(session):
    response = session.get('/todos/1')
    assert response.ok
    assert response.headers['Server'] == 'cloudflare'
from pytest import mark


@mark.testomatio('@T1380940a')
def test_post_1(session):
    response = session.get('/posts/1')
    payload = response.json()
    assert payload['id'] == 1
    assert payload['title'] == 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'
    assert 'recusandae consequuntur expedita' in payload['body']


@mark.testomatio('@T0903dbbc')
def test_post_100(session):
    response = session.get('/posts/100')
    assert response.ok
    payload = response.json()
    assert payload['id'] == 100
    assert payload['title'] == 'at nam consequatur ea labore ea harum'
    assert 'cupiditate quo est a modi' in payload['body']


@mark.testomatio('@Tcfab7801')
def test_headers(session):
    response = session.get('/albums')
    assert response.headers.get('x-powered-by') == 'Express'


@mark.testomatio('@T4feedcda')
def test_timing_posts(session):
    response = session.get('/posts')
    assert response.elapsed.total_seconds() * 1000 < 300
